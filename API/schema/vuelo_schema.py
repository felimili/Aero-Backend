from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VueloSchema(BaseModel):
        id: Optional [int]
        usuario_id: int
        avion_Id: int
        inicio: str
        fin: str
        tiempovuelo: float
        origen: str
        destino: str

#class vuelosRelacionSchema(BaseModel):
#        username: str
#        matricula: str
#        origen: str
#        destino: str
#        tiempoVuelo: float