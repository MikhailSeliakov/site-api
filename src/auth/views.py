from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.users.schemas import PhoneSchema, CodeSchema
from src.auth.service import AuthService, CodeChallenge

router = APIRouter(prefix="/api/v1/login", tags=["Auth"])


@router.post("")
async def login(phone_num: PhoneSchema, session: AsyncSession = Depends(get_async_session)):
    await AuthService(phone_num, session).auth_by_phone()
    return {
        "success": True,
        "status": "Code challenge"
    }


@router.post("/code")
async def code_verify(body: CodeSchema, session: AsyncSession = Depends(get_async_session)):
    jwt_token = await CodeChallenge(body.phone, session).verify_code(body.code)
    # is_user_new = await
    data = {
        "accessToken": jwt_token,
        "tokenType": "Bearer"
    }
    return data
