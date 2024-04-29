from starlette.responses import JSONResponse, Response

from backend.auth.jwt_utils import get_jwt
from backend.auth.models.login_model import Login
from backend.auth.models.register_model import Register

from db.fake_db import users

from fastapi import APIRouter

router = APIRouter()


@router.get("/register")
async def register():
    return {"message": "register"}


@router.post("/register")
async def get_register(register: Register):
    if register.email in users:
        return {"message": "email already registered"}
    if register.password1 == register.password2:
        users[register.email] = {'id': register.id,
                             'username': register.username,
                             'password': register.password1}
        return {"message": "Hello post register", 'info': register}
    else:
        return {"message": "Passwords must be similar"}


@router.get("/login")
async def get_login(login: Login):
    return {"message": "Hello get register"}


@router.post("/login")
async def post_login(login: Login):
    if login.email not in users:
        return {"message": "email isn't registered"}
    if users[login.email]['password'] != login.password:
        return {"message": "incorrect password"}
    user = users[login.email]
    jwt = await get_jwt(user)
    if jwt == 'error':
        return {'message': 'jwt error'}
    content = {"message": "login", 'jwt': user}
    response = JSONResponse(content=content)
    response.set_cookie(key="accessToken", value=jwt)
    return response


@router.get("/logout")
async def register(response: Response):
    response.delete_cookie('accessToken')
    return {"message": "logout success  ", "jwt deleted": 'ok'}
