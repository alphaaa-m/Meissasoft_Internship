from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.db import Base
from app.models.associations import enrollments



class Student(Base):
    __tablename__ = "Students"

    std_id = Column(Integer, primary_key=True)
    std_name = Column(String)
    std_email=Column(String, unique= True)
    department=Column(String)

    courses=relationship('Course', secondary=enrollments, back_populates='students')
