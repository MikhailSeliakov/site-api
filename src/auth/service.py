from random import randint
from fastapi import Depends, HTTPException, status
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import code_challenge
from src.auth.utils import encode_jwt
from src.users.models import users
from src.users.schemas import PhoneSchema
from src.database import get_async_session


class CodeChallenge:
    def __init__(self, phone: str, session: AsyncSession = Depends(get_async_session)):
        self.phone = phone
        self.session = session

    async def start_code_challenge(self):
        delete_stmt = (
            delete(code_challenge)
            .where(code_challenge.c.phone_number == self.phone)
        )
        await self.session.execute(delete_stmt)
        stmt = insert(code_challenge).values(
            phone_number=self.phone,
            code=randint(10000, 99999),
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def verify_code(self, code: int):
        query = (
            select(code_challenge)
            .where(code_challenge.c.phone_number == self.phone)
            .where(code_challenge.c.code == code)
        )
        result = await self.session.execute(query)
        if result.fetchone() is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Проверочный код указан неверно"
            )
        upd_stmt = update(users).where(users.c.phone_number == self.phone).values(is_verified=True)
        await self.session.execute(upd_stmt)
        await self.session.commit()
        query_user_id = select(users).where(users.c.phone_number == self.phone)
        user_id = await self.session.execute(query_user_id)
        jwt_payload = {
            "sub": user_id.first()[0],
            "phone": self.phone,
        }
        return encode_jwt(jwt_payload)


class AuthService:

    def __init__(self, phone: PhoneSchema, session: AsyncSession = Depends(get_async_session)):
        self.phone = phone.phone
        self.session = session

    async def auth_by_phone(self):
        query = select(users).where(users.c.phone_number == self.phone)
        result = await self.session.execute(query)
        if result.first() is None:
            stmt = insert(users).values(phone_number=self.phone)
            await self.session.execute(stmt)
            await self.session.commit()
        await CodeChallenge(phone=self.phone, session=self.session).start_code_challenge()
