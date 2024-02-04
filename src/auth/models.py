from datetime import datetime, timedelta
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()


code_challenge = Table(
    "code_challenge",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", String(length=11)),
    Column("code", Integer),
    Column("expire_time", TIMESTAMP, default=datetime.utcnow() + timedelta(minutes=15)),
    Column("attempt", Integer, default=0),
)
