from fastapi import FastAPI
import uvicorn
from backend.auth import auth_router


app = FastAPI()
app.include_router(
    auth_router.router,
    prefix="/auth",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
