from starlette.responses import Response
from backend.auth.auth_router import router


@router.get("/logout")
async def register(response: Response):
    response.delete_cookie('accessToken')
    return {"message": "logout success  ", "session deleted": 'ok'}
