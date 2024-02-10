import uuid

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import users, users_sports_interests, users_meetings_interests
from src.meetings.models import meetings_interests
from src.sports.models import sports_interests
from src.users.schemas import UserSchema, UserInterests


class UserService:

    def __init__(self, session):
        self.session: AsyncSession = session

    async def is_user_exist(self, user_id: int) -> bool:
        query = select(users).where(users.c.id == user_id)
        result = await self.session.execute(query)
        data = result.mappings().first()
        if data is None:
            return False
        return True

    async def get_profile_info(self, user_id: int) -> UserSchema:
        query = select(users).where(users.c.id == user_id)
        result = await self.session.execute(query)
        data = result.mappings().first()
        return data

    async def is_user_new_reg(self, user_id: int) -> bool:
        query = select(users_meetings_interests).where(users_meetings_interests.c.user_id == user_id)
        query_2 = select(users_sports_interests).where(users_sports_interests.c.user_id == user_id)
        result = await self.session.execute(query)
        result_2 = await self.session.execute(query_2)
        data = result.first()
        data_2 = result_2.first()
        if data is None and data_2 is None:
            return True
        return False

    async def get_user_id_by_phone(self, phone: str) -> int:
        query = select(users.c.id).where(users.c.phone_number == phone)
        result = await self.session.execute(query)
        data = result.first()
        if data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Профиль не найден")
        return data[0]

    async def get_available_interests(self):
        query_meetings = select(meetings_interests).where(meetings_interests.c.is_active == True)
        query_sports = select(sports_interests).where(sports_interests.c.is_active == True)
        result_meetings = await self.session.execute(query_meetings)
        result_sports = await self.session.execute(query_sports)
        available_meetings = result_meetings.mappings().all()
        available_sports = result_sports.mappings().all()
        obj_meetings = []
        for item1 in available_meetings:
            obj_meetings.append({"name": item1.get("interest"), "value": item1.get("interest_ru")})
        obj_sports = []
        for item2 in available_sports:
            obj_sports.append({"name": item2.get("interest"), "value": item2.get("interest_ru")})
        return obj_meetings, obj_sports

    async def update_user_interests(self, user_id: int, body: UserInterests):
        try:
            available_meetings, available_sports = await self.get_available_interests()
            available_meetings_keys = [item.get("name") for item in available_meetings]
            available_sports_keys = [item.get("name") for item in available_sports]

            if not all(item in available_sports_keys for item in body.sports):
                return JSONResponse(status_code=200, content={
                    "success": False,
                    "data": {
                        "message": "Попытка установить несуществующий спортивный интерес",
                        "uuid": uuid.uuid4().hex,
                        "payload": body.sports,
                        "availableInterests": available_sports,
                    }
                })

            if not all(item in available_meetings_keys for item in body.meetings):
                return JSONResponse(status_code=200, content={
                    "success": False,
                    "data": {
                        "message": "Попытка установить несуществующий интерес по встречам",
                        "uuid": uuid.uuid4().hex,
                        "payload": body.meetings,
                        "availableInterests": available_meetings,
                    }
                })

            del_sports = (
                delete(
                    users_sports_interests
                )
                .where(users_sports_interests.c.user_id == user_id)
            )

            del_meetings = (
                delete(
                    users_meetings_interests
                )
                .where(users_meetings_interests.c.user_id == user_id)
            )

            await self.session.execute(del_sports)
            await self.session.execute(del_meetings)

            if len(body.sports) != 0:
                stmt_sports = insert(users_sports_interests).values(
                    [{"user_id": user_id, "interest": item} for item in list(set(body.sports))]
                )
                await self.session.execute(stmt_sports)

            if len(body.meetings) != 0:
                stmt_meetings = insert(users_meetings_interests).values(
                    [{"user_id": user_id, "interest": item} for item in list(set(body.meetings))]
                )
                await self.session.execute(stmt_meetings)

            await self.session.commit()

            return JSONResponse(status_code=200, content={
                "success": True,
                "data": {
                    "message": "Интересы установлены успешно"
                }
            })
        except Exception as e:
            return JSONResponse(status_code=200, content={
                "success": False,
                "data": {
                    "message": "Произошла внутренняя ошибка сервера, если ошибка повторяется, пожалуйста, обратитесь "
                               "в поддержку.",
                    "uuid": uuid.uuid4().hex,
                    "error": str(e)
                }
            })
