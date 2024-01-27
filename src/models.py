from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", Integer),
    Column("first_name", String(length=64)),
    Column("last_name", String(length=64)),
    Column("patronymic_name", String(length=64)),
    Column("location", String(length=64)),
    Column("birth_date", String(length=64)),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("email", String(length=320), unique=True, index=True),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
