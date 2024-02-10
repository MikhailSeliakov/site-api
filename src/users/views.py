from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.schemas import UserSchema, UserInterests
from src.database import get_async_session
from src.users.service import UserService, get_current_auth_user

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.get("/parse-jwt")
async def get_user_info_from_jwt(user: UserSchema = Depends(get_current_auth_user)):
    return {
        "success": True,
        "data": {
            "userId": user.id,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "about": user.about,
        }
    }


@router.get("/interests")
async def get_available_interests(session: AsyncSession = Depends(get_async_session)):
    user_service = UserService(session)
    obj_meetings, obj_sports = await user_service.get_available_interests()
    return {
        "success": True,
        "data": {
            "meetings": obj_meetings,
            "sports": obj_sports,
        }
    }


@router.post("/interests")
async def update_user_interests(
        body: UserInterests,
        user: UserSchema = Depends(get_current_auth_user),
        session: AsyncSession = Depends(get_async_session),
):
    user_service = UserService(session)

    return await user_service.update_user_interests(user.id, body)


@router.get("/{user_id}")
async def get_user_info_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    user_service = UserService(session)
    is_user_exist = await user_service.is_user_exist(user_id)
    if not is_user_exist:
        return JSONResponse(
            status_code=200,
            content={
                "success": False,
                "errors": {
                    "user": "Пользователь не найден!"
                }
            }
        )
    user = await user_service.get_profile_info(user_id)
    user_interests_meetings, user_interests_sports = await user_service.get_user_interests(user_id)
    return {
        "success": True,
        "data": {
            "userId": user.get("id", None),
            "firstName": user.get("first_name", None),
            "lastName": user.get("last_name", None),
            "birthDate": user.get("birth_date", None),
            "about": user.get("about", None),
            "location": user.get("location", None),
            "meetings": user_interests_meetings,
            "sports": user_interests_sports,
        }
    }
