from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.plane_schema import PlaneSchema
from config.db import engine
from model.users import users
from model.planes import planes
from typing import List


plane = APIRouter(prefix="/api/plane",
                  responses={404:{"message": "No encontrado"}})


@plane.get("/", response_model=List[PlaneSchema])
async def get_planes():
    with engine.connect() as conn:
        result = conn.execute(planes.select()).fetchall()

        return result

@plane.get("/{id}", response_model=PlaneSchema)
async def get_plane(id: int):
    with engine.connect() as conn:
        result = conn.execute(planes.select().where(planes.c.id == id)).first()

        return result 


@plane.post("/", status_code=HTTP_201_CREATED)
async def create_plane(data_plane: PlaneSchema):
    with engine.connect() as conn:
        new_plane = data_plane.dict()
        conn.execute(planes.insert().values(new_plane))

        return Response(status_code=HTTP_201_CREATED)



@plane.put("/{id}", status_code=HTTP_200_OK)
async def put_plane(data_update: PlaneSchema, id: str):
    with engine.connect() as conn:
        
        conn.execute(planes.update().values(matricula=data_update.matricula, marca=data_update.marca, 
        modelo=data_update.modelo).where(users.c.id == id))

        return  Response(status_code=HTTP_200_OK)


@plane.delete("/{id}")
async def delete_plane(id: int):
    with engine.connect() as conn:
        conn.execute(planes.delete().where(planes.c.id == id))
        
        return Response(status_code=HTTP_200_OK)