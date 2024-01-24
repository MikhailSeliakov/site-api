import os
import requests
import uuid
from dotenv import load_dotenv
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/oauth", tags=["VK Auth"])

load_dotenv()

ID = os.environ.get("VK_ID")
SECRET = os.environ.get("VK_SECRET")
URL = os.environ.get("BASE_URL")


# https://id.vk.com/auth?uuid=a809fc1a-f86e-11da-bd1a-00112444be1e&app_id=51839264&response_type=silent_token&redirect_uri=https://31.129.96.132


@router.get("")
def get_vk_auth_link():
    request_uuid = uuid.uuid4()
    query_string = f"uuid={request_uuid}&app_id={ID}&response_type=silent_token&redirect_uri={URL}"
    base_link = "https://id.vk.com/auth?" + query_string
    return {
        "url": base_link
    }
