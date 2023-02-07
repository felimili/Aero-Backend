from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.plane_schema import PlaneSchema
from fastapi.encoders import jsonable_encoder
from config.db import engine, sessionmaker
from model.users import users
from model.planes import planes
from typing import List


plane = APIRouter(prefix="/api/plane",
                  responses={404:{"message": "No encontrado"}})


@plane.get("/", response_model=List[PlaneSchema])
async def get_planes():
    
    session = sessionmaker(engine)   
    session = session()      
    result = jsonable_encoder(session.query(planes).all())
    return result
    
    
    #with engine.connect() as conn:
    #    result = conn.execute(planes.select()).fetchall()

    #return result

@plane.get("/{id}", response_model=PlaneSchema)
async def get_plane(id: int):
    session = sessionmaker(engine)   
    session = session()  
    result = jsonable_encoder(session.query(planes).filter(planes.id == id).first())
    return result
    
    
    #with engine.connect() as conn:
    #    result = conn.execute(planes.select().where(planes.c.id == id)).first()

    #    return result 


@plane.post("/", response_model = PlaneSchema, status_code=HTTP_201_CREATED)
async def create_plane(data_plane: PlaneSchema):
    new_plane = planes()
    new_plane.marca = data_plane.marca
    new_plane.matricula = data_plane.matricula
    new_plane.modelo = data_plane.modelo
    session = sessionmaker(engine)
    session = session()
    session.add(new_plane)
    session.commit()
    
    return Response(status_code=HTTP_201_CREATED)  
     
    
    #with engine.connect() as conn:
    #    new_plane = data_plane.dict()
    #    conn.execute(planes.insert().values(new_plane))

    #    return Response(status_code=HTTP_201_CREATED)



@plane.put("/{id}", response_model = PlaneSchema, status_code=HTTP_200_OK)
async def put_plane(data_update: PlaneSchema, id: str):
    
    session = sessionmaker(engine)
    session = session()
    plane_old= session.query(planes).get(id)
    plane_old.marca = data_update.marca
    plane_old.matricula = data_update.matricula
    plane_old.modelo = data_update.modelo
    session.commit()
    
    return  Response(status_code=HTTP_200_OK)
    
    #with engine.connect() as conn:
        
    #    conn.execute(planes.update().values(matricula=data_update.matricula, marca=data_update.marca, 
    #    modelo=data_update.modelo).where(users.c.id == id))

    #    return  Response(status_code=HTTP_200_OK)


@plane.delete("/{id}")
async def delete_plane(id: int):
    
    session = sessionmaker(engine)
    session = session()
    plane_del = session.query(planes).get(id)
    session.delete(plane_del)
    session.commit()
    
    return Response(status_code=HTTP_200_OK)
    
    #with engine.connect() as conn:
    #    conn.execute(planes.delete().where(planes.c.id == id))
        
    #    return Response(status_code=HTTP_200_OK)