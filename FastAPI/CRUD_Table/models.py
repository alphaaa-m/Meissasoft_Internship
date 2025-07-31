from sqlalchemy import Column, Integer, String
from db import Base

class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Item1(Base):
    __tablename__ = "items1"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)