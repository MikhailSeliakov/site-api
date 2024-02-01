from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.users.models import users


router = APIRouter(prefix="/profile", tags=["Auth"])


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.id == user_id)
    result = await session.execute(query)
    print(result.all())
    return {}
