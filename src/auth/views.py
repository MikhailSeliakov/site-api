from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.users.schemas import Phone
from src.auth.service import AuthService

router = APIRouter(prefix="/api/v1/login", tags=["Auth"])


@router.post("")
async def login(phone_num: Phone, session: AsyncSession = Depends(get_async_session)):
    jwt_token = await AuthService(phone_num, session).auth_by_phone()
    return {
        "accessToken": jwt_token,
        "tokenType": "Bearer"
    }
