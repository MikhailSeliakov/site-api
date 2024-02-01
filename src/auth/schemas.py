from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent.parent


class AuthJWT(BaseModel):
    private_key_pem: Path = BASE_DIR / "certs" / "private.pem"
    public_key_pem: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 60
