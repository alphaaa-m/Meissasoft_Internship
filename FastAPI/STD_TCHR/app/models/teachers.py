from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.db import Base



class Teacher(Base):
    __tablename__ = "Teachers"

    tchr_id = Column(Integer, primary_key=True)
    tchr_name = Column(String)
    tchr_email=Column(String, unique= True)
    department=Column(String)

    courses=relationship('Course', back_populates='teachers')
