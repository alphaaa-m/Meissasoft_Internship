from sqlalchemy.orm import Session
from app.models.courses import Course
from app.schemas.crs_schema import Crs_Create, Crs_Update
def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.crs_id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: Crs_Create):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: Crs_Update):
    db_course = db.query(Course).filter(Course.crs_id == course_id).first()
    if db_course:
        for key, value in course.model_dump(exclude_unset=True).items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.crs_id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course