from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BOOLEAN
from config.db import Base



class planes(Base): 
    __tablename__ = "planes"
    id = Column(Integer, primary_key=True, index = True)
    matricula = Column(String(6), nullable=False )
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    
    
    
# Column("afectadoEscuela", BOOLEAN, nullable=False)

# meta_data.create_all(engine)
