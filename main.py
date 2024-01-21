import uvicorn
from fastapi import FastAPI
from src.sports.views import router as sports_router
from src.travels.views import router as travels_router
from src.meetings.views import router as meetings_router
from src.users.views import router as users_router


app = FastAPI()
app.include_router(sports_router)
app.include_router(travels_router)
app.include_router(meetings_router)
app.include_router(users_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
