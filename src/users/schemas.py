from typing import Annotated
from pydantic import BaseModel, StringConstraints


class CreateUser(BaseModel):
    phone: str


class Phone(BaseModel):
    phone: Annotated[str, StringConstraints(pattern=r'^7\d{10}$')]


class Code(BaseModel):
    code: int
