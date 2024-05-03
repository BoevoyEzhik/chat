from fastapi import FastAPI
import uvicorn
from backend.auth.endpoints import auth_app

from backend.db.create_tables import drop_create

app = FastAPI()
app.mount('/auth', auth_app.app)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recreate-db")
async def recreate_db():
    try:
        drop_create()
    except Exception as e:
        print(e)
        return {'status_code': 500,
                'message': 'eternal server error',
                'info': 'Алмазик, мы всё проебали'}
    return {'status_code': 201,
            'message': 'success',
            'info': 'Уронил и поднял дб'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
