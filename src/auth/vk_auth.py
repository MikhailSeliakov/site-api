import os
import requests
import uuid
import json
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/api/v1/oauth", tags=["VK Auth"])

load_dotenv()

ID = os.environ.get("VK_ID")
VK_PROTECTED_KEY = os.environ.get("VK_PROTECTED_KEY")
VK_SERVICE_KEY = os.environ.get("VK_SERVICE_KEY")
URL = os.environ.get("BASE_URL")


@router.get("")
def get_vk_auth_link():
    request_uuid = uuid.uuid4()
    query_string = f"uuid={request_uuid}&app_id={ID}&response_type=silent_token&redirect_uri={URL}/api/v1/oauth/redirect"
    base_link = "https://id.vk.com/auth?" + query_string
    return {
        "url": base_link
    }


@router.get("/redirect")
def handle_vk_credentials(payload):
    try:
        obj = json.loads(payload)
        auth = obj.get("auth")
        token = obj.get("token")
        ttl = obj.get("ttl")
        type = obj.get("type")
        uuid_str = obj.get("uuid")
        link = "https://api.vk.com/method/auth.exchangeSilentAuthToken"
        payload_to_send = {
            "v": "5.131",
            "token": token,
            "access_token": VK_SERVICE_KEY,
            "uuid": uuid_str,
        }
        # r = requests.get(link, params=payload_to_send)
        # print(r.text)
        print({"response":{"access_token":"vk1.a.M4Y83lDVeQrCoY6RwdWz8bvZu1pbdpvC5MyQGuNenVyRJxZZ0Uze_qo0lvXqlpTudn-7pwvVY1R02VpNPgiNAUyDRIbAH5MZyKxnBhCPhqDvokukTGXI3OSimwm0Alu-T0pkS-IRmOopd8GXWH5INLMwiy0yWFrG2rlGUxcGOebw_asgsg9NjtlmPPyAzc_3n7oNBJiZGbgZ0SqkYDGhFA","access_token_id":"53550841","user_id":125604216,"additional_signup_required":False,"is_partial":False,"is_service":False,"source":1,"source_description":"Silent authentication","expires_in":31536000}})

        return RedirectResponse(
            url=URL
        )
    except Exception as e:
        return {
            "success": False,
            "exception": e
        }
