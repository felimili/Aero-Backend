from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.vuelo_schema import VueloSchema
from fastapi.encoders import jsonable_encoder
from config.db import engine, sessionmaker
from model.vuelos import vuelos
from model.users import users
from model.planes import planes
from typing import List


vuelo = APIRouter(prefix="/api/vuelo",
                  responses={404:{"message": "No encontrado"}})

@vuelo.get("/", status_code=HTTP_200_OK)
async def get_vuelos():
    
    session = sessionmaker(engine)   
    session = session() 
    
    result = jsonable_encoder(session.query(
        vuelos.id, users.apellido, users.nombre, planes.matricula, vuelos.inicio, vuelos.fin, vuelos.origen, vuelos.destino, vuelos.tiempovuelo
            ).filter(
            vuelos.usuario_id == users.id
            ).filter(
            vuelos.avion_id == planes.id
            ).all())
    return result
    
    #with engine.connect() as conn:
    #    result = conn.execute('select vuelos.id, apellido, nombre, matricula, inicio, fin, origen, destino, tiempoVuelo from vuelos inner join users on vuelos.usuario_id = users.id inner join planes on vuelos.avion_id = planes.id order by inicio asc').fetchall()
        
    #    return result
    
@vuelo.get("/{id}")
async def get_vuelo(id: int):
    
    session = sessionmaker(engine)   
    session = session()  
    result = jsonable_encoder(session.query(vuelos).get(id))
    return result
    
    
    #with engine.connect() as conn:
    #    result = conn.execute(vuelos.select().where(vuelos.c.id == id)).first()
    #    return result
    
@vuelo.post("/", response_model=VueloSchema, status_code=HTTP_201_CREATED)
async def create_vuelo(data_vuelo: VueloSchema):
    
    new_vuelo = vuelos()
         
    new_vuelo.usuario_id =data_vuelo.usuario_id
    new_vuelo.avion_id  = data_vuelo.avion_Id
    new_vuelo.inicio = data_vuelo.inicio
    new_vuelo.fin = data_vuelo.fin
    new_vuelo.origen = data_vuelo.origen
    new_vuelo.destino = data_vuelo.destino
    new_vuelo.tiempoVuelo = data_vuelo.tiempoVuelo
    
    session = sessionmaker(engine)
    session = session()
    session.add(new_vuelo)
    session.commit()
    
    return Response(status_code=HTTP_201_CREATED)
    
    #with engine.connect() as conn:
    #    new_vuelo = data_vuelo.dict()
    #    conn.execute(vuelos.insert().values(new_vuelo))
    #    return Response(status_code=HTTP_201_CREATED)
        
@vuelo.delete("/{id}")
async def delete_vuelo(id: int):
    
    session = sessionmaker(engine)
    session = session()
    vuelo_del = session.query(vuelos).get(id)
    session.delete(vuelo_del)
    session.commit()
    
    return Response(status_code=HTTP_200_OK)
    #with engine.connect() as conn:
    #    conn.execute(vuelos.delete().where(vuelos.c.id == id))
        
    #    return Response(status_code=HTTP_200_OK)


@vuelo.put("/{id}", response_model=VueloSchema)
async def put_vuelo(data_update: VueloSchema, id: str):
    
    session = sessionmaker(engine)
    session = session()
    vuelo_old = session.query(vuelos).get(id)
      
    vuelo_old.usuario_id =data_update.usuario_id
    vuelo_old.avion_id  = data_update.avion_Id
    vuelo_old.inicio = data_update.inicio
    vuelo_old.fin = data_update.fin
    vuelo_old.origen = data_update.origen
    vuelo_old.destino = data_update.destino
    vuelo_old.tiempoVuelo = data_update.tiempoVuelo
    session.commit()
    
    return  Response(status_code=HTTP_200_OK)
    
    
    #with engine.connect() as conn:
    #    conn.execute(vuelos.update().values(usuario_id=data_update.usuario_id, avion_Id=data_update.avion_Id, inicio=data_update.inicio, fin=data_update.fin,origen=data_update.origen, destino=data_update.destino,tiempoVuelo=data_update.tiempoVuelo).where(vuelos.c.id == id))
    #    return Response(status_code=HTTP_200_OK)
        
        
#ok