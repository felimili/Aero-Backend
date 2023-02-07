from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.status import HTTP_202_ACCEPTED,HTTP_401_UNAUTHORIZED
from jose import jwt, JWTError
from config.db import engine, sessionmaker
from fastapi.encoders import jsonable_encoder
from model.users import users
from werkzeug.security import check_password_hash
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 5
SECRET = "GN20FDX6c9HEOAi5oSHNssAuI4bvhUfRBRRseow"

auth_jwt = APIRouter()

crypt = CryptContext(schemes=["bcrypt"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

def search_user(username: str):
    user_find = users()
    session = sessionmaker(engine)   
    session = session()  
    
    user_find = session.query(users).filter(users.username == username).first()
    
    if not user_find:
            raise HTTPException(status_code=400, detail="Usuario no es correcto")
    
    return user_find
        
    #with engine.connect() as conn:
    #    result = conn.execute(users.select().where(users.c.username == username)).first()
              
    #    return result

async def auth_user(token: str = Depends(oauth2)):
    
    execption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticas invalidas",
        headers={"www-Authenticate": "Bearer"}) 
    
    try:
        
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        
        if username is None:
            raise execption
    
    except JWTError:
            raise execption
    
    return search_user(username)

@auth_jwt.get ("/api/check_sesion")
async def check(token: str = Depends(oauth2)):
      
    try:
            
        valido = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
               
    except JWTError:
            return Response(status_code=HTTP_401_UNAUTHORIZED)
    
    return Response(status_code=HTTP_202_ACCEPTED)





@auth_jwt.post ("/api/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_check = users()
    user_check = search_user(form.username)
    
    check_pass = check_password_hash(user_check.password, form.password)  
               
    if not check_pass:
       raise HTTPException(status_code=401, detail="Constraseña no es correcta")
        
    access_token ={"sub": user_check.username,
                       "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION) }

    #refresh_token ={"sub": username[1], "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION) }

    return {"access_token": jwt.encode(access_token, SECRET,  algorithm=ALGORITHM), "token_type": "bearer",}
   
    


@auth_jwt.get("/api/me")
async def me(user: users = Depends(auth_user)):
    return user

