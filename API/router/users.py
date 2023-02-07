from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.user_schema import UserSchema
from config.db import engine, sessionmaker
from model.users import users
from werkzeug.security import generate_password_hash
from fastapi.encoders import jsonable_encoder
from typing import List
from passlib.context import CryptContext



user = APIRouter(prefix="/api/user",
                  responses={404:{"message": "No encontrado"}})

crypt = CryptContext(schemes=["bcrypt"])


@user.get("/", response_model=List[UserSchema],status_code=HTTP_200_OK)
async def get_users():
    session = sessionmaker(engine)   
    session = session()      
    result = jsonable_encoder(session.query(users).all())
    return result


@user.get("/{id}", response_model=UserSchema)
async def get_user(id: int): 
    session = sessionmaker(engine)   
    session = session()  
    result = jsonable_encoder(session.query(users).get(id))
    return result


@user.post("/", response_model=UserSchema,status_code=HTTP_201_CREATED)
async def create_user(data_user: UserSchema):
    
    new_user = users()
    new_user.password = generate_password_hash(data_user.password, "pbkdf2:sha256:30",30)
    new_user.apellido = data_user.apellido
    new_user.email = data_user.email
    new_user.nombre = data_user.nombre
    new_user.username = data_user.username
    session = sessionmaker(engine)
    session = session()
    session.add(new_user)
    session.commit()
    

    return Response(status_code=HTTP_201_CREATED)



@user.put("/{id}", response_model=UserSchema)
async def put_user(data_update: UserSchema, id: str):
    
    session = sessionmaker(engine)
    session = session()
    user_old= session.query(users).get(id)
      
    user_old.password = generate_password_hash(data_update.password, "pbkdf2:sha256:30",30)
    user_old.username  = data_update.username
    user_old.apellido = data_update.apellido
    user_old.nombre = data_update.nombre
    user_old.email = data_update.email
    session.commit()
    
    #with engine.connect() as conn:
        
    #    encrip = generate_password_hash(data_update.password, "pbkdf2:sha256:30",30)
    #    conn.execute(users.update().values(username=data_update.username, nombre=data_update.nombre, apellido=data_update.apellido, email=data_update.email, password=encrip).where(users.c.id == id))

    return  Response(status_code=HTTP_200_OK)

@user.delete("/{id}")
async def delete_user(id: int):
    
    session = sessionmaker(engine)
    session = session()
    user_del = session.query(users).get(id)
    session.delete(user_del)
    session.commit()
    
    #user_old= session.query(users).get(id)
    #with engine.connect() as conn:
    #    conn.execute(users.delete().where(users.c.id == id))
        
    return Response(status_code=HTTP_200_OK)


 