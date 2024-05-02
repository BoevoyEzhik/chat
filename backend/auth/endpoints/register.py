from backend.auth.models.register_model import Register
from backend.auth.password_utils import generating_hash
from backend.db.users.create import create_user
from fastapi import APIRouter

from backend.db.users.read import read_user

register_router = APIRouter()


@register_router.get("/register")
async def register():
    return {'status_code': 200,
            "message": "Hello get register",
            "info": "register page"}


@register_router.post("/register")
async def register(register_user: Register):
    user = read_user(register_user.email)
    if user:
        return {'status_code': 403,
                "message": "Hello post register",
                'info': 'email has already registered'}
    info = {'username': register_user.username,
            'email': register_user.email,
            'password': await generating_hash(register_user.password1)}
    create_user(info)
    return {'status_code': 201,
            "message": "Hello post register",
            'info': 'register success'}
