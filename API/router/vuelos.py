from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.vuelo_schema import VueloSchema
from config.db import engine
from model.vuelos import vuelos
from typing import List


vuelo = APIRouter(prefix="/api/vuelo",
                  responses={404:{"message": "No encontrado"}})

@vuelo.get("/")
async def get_vuelos():
    
    with engine.connect() as conn:
        result = conn.execute('select vuelos.id, apellido, nombre, matricula, inicio, fin, origen, destino, tiempoVuelo from vuelos inner join users on vuelos.usuario_id = users.id inner join planes on vuelos.avion_id = planes.id order by inicio asc').fetchall()
        
        return result
    
@vuelo.get("/{id}")
async def get_vuelo(id: int):
    with engine.connect() as conn:
        result = conn.execute(vuelos.select().where(vuelos.c.id == id)).first()
        return result
    
@vuelo.post("/", response_model=VueloSchema, status_code=HTTP_201_CREATED)
async def create_vuelo(data_vuelo: VueloSchema):
    
    with engine.connect() as conn:
        new_vuelo = data_vuelo.dict()
        conn.execute(vuelos.insert().values(new_vuelo))
        return Response(status_code=HTTP_201_CREATED)
        
@vuelo.delete("/{id}")
async def delete_vuelo(id: int):
    with engine.connect() as conn:
        conn.execute(vuelos.delete().where(vuelos.c.id == id))
        
        return Response(status_code=HTTP_200_OK)


@vuelo.put("/{id}")
async def put_vuelo(data_update: VueloSchema, id: str):
    with engine.connect() as conn:
        conn.execute(vuelos.update().values(usuario_id=data_update.usuario_id, avion_Id=data_update.avion_Id, inicio=data_update.inicio, fin=data_update.fin,origen=data_update.origen, destino=data_update.destino,tiempoVuelo=data_update.tiempoVuelo).where(vuelos.c.id == id))
        return Response(status_code=HTTP_200_OK)
        