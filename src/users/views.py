from typing import Annotated
from fastapi import APIRouter, Path


router = APIRouter(prefix="/api/v1/login", tags=["Auth"])


@router.post("")
def login(phone: str):
    return {
        "phone": phone
    }

