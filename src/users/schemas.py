from typing import Annotated, Dict
from pydantic import BaseModel, StringConstraints, Field


class UserSchema(BaseModel):
    id: int
    phone_number: str
    first_name: str | None
    last_name: str | None
    patronymic_name: str | None
    location: str | None
    birth_date: str | None
    about: str | None
    is_active: bool
    is_verified: bool


class PhoneSchema(BaseModel):
    phone: Annotated[str, StringConstraints(pattern=r'^7\d{10}$')]


class CodeSchema(BaseModel):
    phone: Annotated[str, StringConstraints(pattern=r'^7\d{10}$')]
    code: int = Field(..., ge=0, le=99999)


class InterestSportSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool


class InterestMeetingSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool


class InterestTravelSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool
