from pydantic import BaseModel


class InterestSportSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool
