from pydantic import BaseModel


class CreateUser(BaseModel):
    phone: str
