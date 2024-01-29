from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", String(length=11)),
    Column("first_name", String(length=64)),
    Column("last_name", String(length=64)),
    Column("patronymic_name", String(length=64)),
    Column("location", String(length=64)),
    Column("birth_date", String(length=64)),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class UserDB:

    id = Column(Integer, primary_key=True)
    phone_number = Column(String(length=11))
    first_name = Column(String(length=64))
    last_name = Column(String(length=64))
    patronymic_name = Column(String(length=64))
    location = Column(String(length=64))
    birth_date = Column(String(length=64))
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
