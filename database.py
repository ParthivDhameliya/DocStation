from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# db_user = "postgres"
# db_password = "Kunalgoyal26@!"
# db_url = "localhost"
# db_name = "DocAuto"
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Dhameliya8548@localhost/DocAuto'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
