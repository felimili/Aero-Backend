from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from config.db import Base

class vuelos(Base):
    __tablename__ = "vuelos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('users.id'))
    avion_id = Column(Integer, ForeignKey('planes.id'))
    inicio = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable=False)
    tiempovuelo= Column(Float, nullable=False)
    origen = Column(String(5), nullable=False)
    destino = Column(String(5), nullable=False)

#meta_data.create_all(engine)