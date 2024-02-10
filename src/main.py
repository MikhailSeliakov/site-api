import os
import sys

sys.path.append(os.getcwd())

import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from auth.vk_auth import router as vk_router
from auth.views import router as auth_router
from sports.views import router as sports_router
from travels.views import router as travels_router
from meetings.views import router as meetings_router
from users.views import router as users_router


app = FastAPI(title="Да! Погнали)")
# app.include_router(sports_router)
# app.include_router(travels_router)
app.include_router(meetings_router)
app.include_router(users_router)
# app.include_router(vk_router)
app.include_router(auth_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder({
            "success": False,
            "detail": exc.errors(),
        }),
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
