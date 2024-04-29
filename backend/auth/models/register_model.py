from pydantic import BaseModel
from uuid import uuid4


class Register(BaseModel):
    id: uuid4 = str(uuid4())
    email: str
    username: str
    password1: str
    password2: str
