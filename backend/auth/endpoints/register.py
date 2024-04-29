from backend.auth.auth_router import router
from backend.auth.models.register_model import Register


@router.get("/register")
async def register():
    return {"message": "register"}


@router.post("/register")
async def register(info: Register):
    return {"message": "Hello post register", 'info': info}
