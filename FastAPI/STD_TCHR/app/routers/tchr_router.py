from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.tchr_schema import Teacher, Tchr_Create, Tchr_Update
from app.crud import tchr_crud

router = APIRouter(
    prefix="/teachers",
    tags=["teachers"],
    responses={404: {"description": "Teacher not found"}},
)

@router.post("/", response_model=Teacher, status_code=status.HTTP_201_CREATED)
def create_teacher_route(teacher: Tchr_Create, db: Session = Depends(get_db)):
    try:
        return tchr_crud.create_teacher(db=db, teacher=teacher)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating teacher: {e}")

@router.get("/{teacher_id}", response_model=Teacher)
def read_teacher_route(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = tchr_crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@router.put("/{teacher_id}", response_model=Teacher)
def update_teacher_route(teacher_id: int, teacher: Tchr_Update, db: Session = Depends(get_db)):
    # IMPORTANT: Uniqueness check for email on update removed.
    db_teacher = tchr_crud.update_teacher(db, teacher_id=teacher_id, teacher=teacher)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@router.delete("/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher_route(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = tchr_crud.delete_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return None