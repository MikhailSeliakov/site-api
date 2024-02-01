from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()


code_challenge = Table(
    "code_challenge",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", String(length=11)),
    Column("code", String(length=5)),
    Column("expire_time", TIMESTAMP),
)
