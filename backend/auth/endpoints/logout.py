from starlette.responses import Response
from fastapi import APIRouter


logout_router = APIRouter()


@logout_router.get("/logout")
async def logout(response: Response):
    response.delete_cookie('accessToken')
    return {'status_code': 200,
            "message": "logout success",
            "info": 'token deleted'}
