from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BOOLEAN
from config.db import Base, engine
from sqlalchemy.orm import relationship



class planes(Base): 
    __tablename__ = "planes"
    id = Column(Integer, primary_key=True, index = True)
    matricula = Column(String(6), nullable=False )
    marca = Column(String(45), nullable=False)
    modelo = Column(String(45), nullable=False)
    #planevuelo = relationship("vuelos", back_populates = "planes")
    
    
    
# Column("afectadoEscuela", BOOLEAN, nullable=False)

    Base.metadata.create_all(bind=engine)
