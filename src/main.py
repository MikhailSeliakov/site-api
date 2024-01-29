import os
import sys
sys.path.append(os.getcwd())

import uvicorn
from fastapi import FastAPI
from auth.vk_auth import router as vk_router
from sports.views import router as sports_router
from travels.views import router as travels_router
from meetings.views import router as meetings_router
from users.views import router as users_router


app = FastAPI(title="Да! Погнали)")
app.include_router(sports_router)
app.include_router(travels_router)
app.include_router(meetings_router)
app.include_router(users_router)
app.include_router(vk_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
