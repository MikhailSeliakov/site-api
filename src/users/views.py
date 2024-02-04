import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.auth.utils import decode_jwt
from src.users.schemas import UserSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import users
from src.database import get_async_session


http_bearer = HTTPBearer()
router = APIRouter(prefix="/profile", tags=["Auth"])


async def get_current_token_payload(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
):
    token = credentials.credentials
    payload = decode_jwt(token)
    return payload


async def get_current_auth_user(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(get_async_session)
) -> UserSchema:
    user_id = payload.get("sub")
    query = select(users).where(users.c.id == user_id)
    result = await session.execute(query)
    user_obj = result.first()
    if user_obj is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"X-uuid": uuid.uuid4().hex}
        )
    return user_obj


@router.get("/me")
async def get_user_info(user: UserSchema = Depends(get_current_auth_user)):
    return {
        "userId": user.id,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "about": user.about,
    }
