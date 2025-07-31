from sqlalchemy.orm import Session
from app.models.teachers import Teacher
from app.schemas.tchr_schema import Tchr_Create, Tchr_Update

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.tchr_id == teacher_id).first()

def create_teacher(db: Session, teacher: Tchr_Create):
    db_teacher = Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def update_teacher(db: Session, teacher_id: int, teacher: Tchr_Update):
    db_teacher = db.query(Teacher).filter(Teacher.tchr_id == teacher_id).first()
    if db_teacher:
        for key, value in teacher.model_dump(exclude_unset=True).items():
            setattr(db_teacher, key, value)
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.tchr_id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher