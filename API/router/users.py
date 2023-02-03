from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from schema.user_schema import UserSchema
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash
from typing import List
from passlib.context import CryptContext



user = APIRouter(prefix="/api/user",
                  responses={404:{"message": "No encontrado"}})

crypt = CryptContext(schemes=["bcrypt"])


@user.get("/", response_model=List[UserSchema], status_code=HTTP_200_OK)
async def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        
        return result


@user.get("/{id}", response_model=UserSchema)
async def get_user(id: int): 
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == id)).first()

        return result


@user.post("/", response_model=UserSchema,status_code=HTTP_201_CREATED)
async def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30",30)
        conn.execute(users.insert().values(new_user))

        return Response(status_code=HTTP_201_CREATED)



@user.put("/{id}", response_model=UserSchema)
async def put_user(data_update: UserSchema, id: str):
    with engine.connect() as conn:
        
        encrip = generate_password_hash(data_update.password, "pbkdf2:sha256:30",30)
        conn.execute(users.update().values(username=data_update.username, nombre=data_update.nombre, apellido=data_update.apellido, email=data_update.email, password=encrip).where(users.c.id == id))

        return  Response(status_code=HTTP_200_OK)

@user.delete("/{id}")
async def delete_user(id: int):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == id))
        
        return Response(status_code=HTTP_200_OK)


 