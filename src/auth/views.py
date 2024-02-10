from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.users.schemas import PhoneSchema, CodeSchema
from src.auth.service import AuthService, CodeChallenge
from src.users.service import UserService

router = APIRouter(prefix="/api/v1/login", tags=["Auth"])


@router.post("")
async def login(phone_num: PhoneSchema, session: AsyncSession = Depends(get_async_session)):
    await AuthService(phone_num, session).auth_by_phone()
    return {
        "success": True,
        "data": {
            "status": "Code challenge"
        }
    }


@router.post("/code")
async def code_verify(body: CodeSchema, session: AsyncSession = Depends(get_async_session)):
    user_service = UserService(session)
    is_code_valid = await CodeChallenge(body.phone, session).verify_code(body.code)
    if not is_code_valid:
        return JSONResponse(
            status_code=200,
            content={
                "success": False,
                "errors": {
                    "code": "Проверочный код указан неверно!"
                }
            }
        )
    user_id = await user_service.get_user_id_by_phone(body.phone)
    jwt_token = await AuthService.get_jwt_token_by_user_id(user_id, body.phone)
    is_user_new = await user_service.is_user_new_reg(user_id)
    return {
        "success": True,
        "data": {
            "accessToken": jwt_token,
            "tokenType": "Bearer",
            "isNewUser": is_user_new
        }
    }
