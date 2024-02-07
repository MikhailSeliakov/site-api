from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean


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
    Column("about", String(length=1024)),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


meeting_interests = Table(
    "meeting_interests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("interest", String),
    Column("interest_ru", String),
    Column("is_active", Boolean),
)

sport_interests = Table(
    "sport_interests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("interest", String),
    Column("interest_ru", String),
    Column("is_active", Boolean),
)
