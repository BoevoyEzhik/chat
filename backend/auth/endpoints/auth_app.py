from fastapi import FastAPI
from backend.auth.endpoints.register import register_router
from backend.auth.endpoints.login import login_router
from backend.auth.endpoints.logout import logout_router


app = FastAPI()
app.include_router(register_router)
app.include_router(login_router)
app.include_router(logout_router)

