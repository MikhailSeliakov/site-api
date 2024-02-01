import jwt
from src.config import settings
from datetime import datetime


def encode_jwt(
        payload: dict,
        private_key: str = settings.auth_jwt.private_key_pem.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
        expire_minutes: int = settings.auth_jwt.access_token_expire_minutes
):
    to_encode = payload.copy()
    expire = expire_minutes
    now = datetime.utcnow()
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
    decoded = jwt.decode(jwt_token, public_key, algorithms=[algorithm])
    return decoded

