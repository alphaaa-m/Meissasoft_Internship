from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.std_schema import Student, Std_Create, Std_Update
from app.crud import std_crud

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Student not found"}},
)

@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student_route(student: Std_Create, db: Session = Depends(get_db)):
    try:
        return std_crud.create_student(db=db, student=student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating student: {e}")
    

@router.get("/{student_id}", response_model=Student)
def read_student_route(student_id: int, db: Session = Depends(get_db)):
    db_student = std_crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.put("/{student_id}", response_model=Student)
def update_student_route(student_id: int, student: Std_Update, db: Session = Depends(get_db)):
    db_student = std_crud.update_student(db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_route(student_id: int, db: Session = Depends(get_db)):
    db_student = std_crud.delete_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return None