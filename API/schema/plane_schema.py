from pydantic import BaseModel
from typing import Optional


class PlaneSchema(BaseModel):
    id: Optional[int]
    matricula: str
    marca: str
    modelo: str
