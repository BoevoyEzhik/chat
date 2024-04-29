#from auth.auth_router import router
from backend.auth.models.register_model import Register
from db.insert import insert_user

from fastapi import APIRouter

router = APIRouter()


@router.get("/register")
async def register():
    return {"message": "register"}


@router.post("/register")
async def register(info: Register):
    if info.password1 == info.password2:
        print(info, type(info))
        insert_user(info)
        return {"message": "Hello post register", 'info': info}
    else:
        return {"message": "Passwords must be similar"}
