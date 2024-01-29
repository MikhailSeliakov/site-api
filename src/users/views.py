from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.users.models import users
from src.users.schemas import Phone

router = APIRouter(prefix="/api/v1/login", tags=["Auth"])


@router.post("")
async def login(phone_num: Phone, session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.phone_number == phone_num.phone)
    result = await session.execute(query)
    if result.first() is None:
        stmt = insert(users).values(phone_number=phone_num.phone)
        await session.execute(stmt)
        await session.commit()
    return {
        "status": "success"
    }


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.id == user_id)
    result = await session.execute(query)
    print(result.all())
    return {}
