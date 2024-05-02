from starlette.responses import JSONResponse

from backend.auth.password_utils import is_valid_password
from backend.db.users.read import read_user
from backend.auth.jwt_utils import get_jwt
from backend.auth.models.login_model import Login
from fastapi import APIRouter


login_router = APIRouter()


@login_router.get("/login")
async def get_login():
    return {'status_code': 200,
            "message": "Hello get login"}


@login_router.post("/login")
async def post_login(login_info: Login):
    user = read_user(login_info.email)
    if not user:
        return {'status_code': 404,
                "message": "Hello post login",
                'info': 'email not registered'}
    if not await is_valid_password(login_info.password, user.password):
        return {'status_code': 403,
                "message": "Hello post login",
                'info': 'wrong password'}
    jwt = await get_jwt({'id': str(user.id),
                   'username': user.username})
    content = {'status_code': 200,
               "message": "login"}
    response = JSONResponse(content=content)
    response.set_cookie(key="accessToken", value=jwt)
    return response
