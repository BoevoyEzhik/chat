from starlette.responses import JSONResponse

from backend.auth.auth_router import router
from backend.auth.models.login_model import Login


@router.get("/login")
async def register():
    jwt = await get_jwt()
    content = {"message": "login"}
    response = JSONResponse(content=content)
    response.set_cookie(key="accessToken", value=jwt)
    return response


@router.post("/login")
async def register(info: Login):
    return {"message": "Hello post register", 'info': info}