from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.db import Base

enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", ForeignKey("Students.std_id"), primary_key=True),
    Column("course_id", ForeignKey("Courses.crs_id"), primary_key=True)
)