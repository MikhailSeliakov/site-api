from fastapi import HTTPException, status
from sqlalchemy import select
from src.users.models import users, users_interests
from src.users.schemas import UserSchema


class UserService:

    def __init__(self, session):
        self.session = session

    async def get_profile_info(self, user_id: int) -> UserSchema:
        query = select(users).where(users.c.id == user_id)
        result = await self.session.execute(query)
        data = result.first()
        if data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Профиль не найден")
        return data

    async def is_user_new_reg(self, user_id: int) -> bool:
        query = select(users_interests).where(users_interests.c.user_id == user_id)
        result = await self.session.execute(query)
        data = result.first()
        if data is None:
            return True
        return False

    async def get_user_id_by_phone(self, phone: str) -> int:
        query = select(users.c.id).where(users.c.phone_number == phone)
        result = await self.session.execute(query)
        data = result.first()
        if data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Профиль не найден")
        return data[0]
