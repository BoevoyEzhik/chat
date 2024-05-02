from pydantic import BaseModel
from uuid import uuid4


class Register(BaseModel):
    email: str
    username: str
    password1: str
    password2: str
