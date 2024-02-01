from datetime import datetime
from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.utils import encode_jwt
from src.users.models import users
from src.users.schemas import Phone
from src.database import get_async_session


class CodeChallenge:
    def __init__(self, phone: Phone):
        self.phone = phone
        self.expire_time = datetime.utcnow

    async def start_code_challenge(self):
        pass


class AuthService:

    def __init__(self, phone: Phone, session: AsyncSession = Depends(get_async_session)):
        self.phone = phone.phone
        self.session = session

    async def auth_by_phone(self):
        query = select(users).where(users.c.phone_number == self.phone)
        result = await self.session.execute(query)
        if result.first() is None:
            stmt = insert(users).values(phone_number=self.phone)
            await self.session.execute(stmt)
            await self.session.commit()
        query_user_id = select(users).where(users.c.phone_number == self.phone)
        user_id = await self.session.execute(query_user_id)
        jwt_payload = {
            "sub": user_id.first()[0],
            "phone": self.phone,
        }
        return encode_jwt(jwt_payload)
        # await CodeChallenge(self.phone).start_code_challenge()
