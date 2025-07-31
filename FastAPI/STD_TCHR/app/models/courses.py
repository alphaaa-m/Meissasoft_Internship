from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from app.models.associations import enrollments

class Course(Base):
    __tablename__ = "Courses"

    crs_id = Column(Integer, primary_key=True)
    crs_title = Column(String)
    crs_code = Column(String, unique=True)
    tchr_id = Column(Integer, ForeignKey("Teachers.tchr_id"))
    department= Column(String)

    teachers = relationship("Teacher", back_populates="courses")
    students = relationship("Student", secondary=enrollments, back_populates="courses")
