from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, BOOLEAN
from config.db import Base, engine
from sqlalchemy.orm import relationship



class users(Base):
     __tablename__ = "users"
    
     id = Column(Integer, primary_key=True)
     username = Column(String(40), nullable=False)
     password = Column(String(255), nullable=False)
     nombre = Column(String(40), nullable=False)
     apellido = Column(String(40), nullable=False)
     email = Column(String(40), nullable=False)
     #prueba = Column(String(40), nullable=False)
     #uservuelo = relationship("vuelos", back_populates = "users")

     def __str__(self):
          return self.password
     
     
if __name__ == '__main__':
     
     #Base.metadata.drop_all(engine)
     Base.metadata.create_all(bind=engine)

            
  

