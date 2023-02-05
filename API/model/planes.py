from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BOOLEAN
from config.db import engine, meta_data



planes = Table("planes", meta_data,
            Column("id", Integer, primary_key=True),
            Column("matricula", String(6), nullable=False ),
            Column("marca", String(50), nullable=False),
            Column("modelo", String(50), nullable=False))
            #Column("afectadoEscuela", BOOLEAN, nullable=False))

meta_data.create_all(engine)
