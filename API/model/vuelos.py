from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from config.db import engine, meta_data

vuelos = Table("vuelos", meta_data,
            Column("id", Integer, primary_key=True),
            Column("usuario_id", Integer, ForeignKey('users.id')),
            Column("avion_Id", Integer, ForeignKey('planes.id')),
            Column('inicio', DateTime, nullable=False),
            Column('fin', DateTime, nullable=False),
            Column('tiempoVuelo', Float, nullable=False),
            Column('origen', String(5), nullable=False),
            Column('destino', String(5), nullable=False))

meta_data.create_all(engine)