from pydantic import BaseModel
from uuid import uuid4


class Register(BaseModel):
    id: uuid4 = uuid4()
    email: str
    password1: str
    password2: str