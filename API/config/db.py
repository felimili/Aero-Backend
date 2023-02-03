from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:A12345678$@localhost:3306/aero")


meta_data = MetaData()