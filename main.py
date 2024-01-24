import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead
from src.sports.views import router as sports_router
from src.travels.views import router as travels_router
from src.meetings.views import router as meetings_router
from src.users.views import router as users_router
from auth.vk_auth import router as vk_router

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(title="Да! Погнали)")
app.include_router(sports_router)
app.include_router(travels_router)
app.include_router(meetings_router)
app.include_router(users_router)
app.include_router(vk_router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)




