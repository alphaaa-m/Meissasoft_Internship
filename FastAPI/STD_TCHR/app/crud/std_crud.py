from sqlalchemy.orm import Session
from app.models.students import Student
from app.schemas.std_schema import Std_Create, Std_Update


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.std_id == student_id).first()

def create_student(db: Session, student: Std_Create):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: Std_Update):
    db_student = db.query(Student).filter(Student.std_id == student_id).first()
    if db_student:
        for key, value in student.model_dump(exclude_unset=True).items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.std_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student