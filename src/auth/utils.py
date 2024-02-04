import jwt
from datetime import datetime, timedelta
from jwt import PyJWTError
from fastapi import HTTPException, status
from src.config import settings


def encode_jwt(
        payload: dict,
        private_key: str = settings.auth_jwt.private_key_pem.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
        expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
        expire_timedelta: timedelta | None = None
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
        jwt_token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_pem.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
):
    try:
        decoded = jwt.decode(jwt_token, public_key, algorithms=[algorithm])
        return decoded
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен указан некорректно")
