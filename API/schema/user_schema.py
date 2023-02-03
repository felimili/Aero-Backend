from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int]
    username:  str
    password: str
    nombre: str
    apellido: str
    email: str







