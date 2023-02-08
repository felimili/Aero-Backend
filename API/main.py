from fastapi import FastAPI
from router.planes import  plane
from router.users import user
from config.db import Base, engine
from router.jwt_auth_users import auth_jwt
from router.vuelos import vuelo
from router.upload import upload
# Iniciar Server: uvicorn main:app --reload

Base.metadata.create_all(bind=engine)

tags_metadata = [
            {
                "name": "users",
            },
            {
                "name": "planes",
            },
            {
                "name": "vuelos",
            }
]


app = FastAPI()


app.include_router(plane)
app.include_router(user)
app.include_router(auth_jwt)
app.include_router(vuelo)
app.include_router(upload)

 