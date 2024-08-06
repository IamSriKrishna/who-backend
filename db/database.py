from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://postgres:2004@localhost:3000/inventory"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False,bind=engine)

Base = declarative_base()

def get_DB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()