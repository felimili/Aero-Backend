#from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://root:A12345678$@localhost:3306/aero")


#meta_data = MetaData()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:A12345678$@localhost:3306/aero"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()