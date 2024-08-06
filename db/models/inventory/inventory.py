from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import ARRAY

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,unique=True)
    description = Column(String,nullable=False)
    image=  Column(String,nullable=False)
    stock= Column(Integer,nullable=False)
    amount= Column(Integer,nullable=False)
    info= Column(ARRAY(String),nullable=False)
    