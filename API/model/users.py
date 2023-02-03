from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BOOLEAN
from config.db import engine, meta_data


users = Table("users", meta_data,
            Column("id", Integer, primary_key=True),
            Column("username", String(40), nullable=False),
            Column("password", String(255), nullable=False),
            Column("nombre", String(30), nullable=False),
            Column("apellido", String(30), nullable=False),
            Column("email", String(30), nullable=False))
            #Column("alumno", BOOLEAN, nullable = False))
            
  

meta_data.create_all(engine)
