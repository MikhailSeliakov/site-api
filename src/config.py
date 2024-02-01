import os
from dotenv import load_dotenv

from src.auth.schemas import AuthJWT

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")


class Settings(AuthJWT):
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
