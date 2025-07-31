from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.crs_schema import Course, Crs_Create, Crs_Update
from app.crud import crs_crud

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    responses={404: {"description": "Course not found"}},
)

@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course_route(course: Crs_Create, db: Session = Depends(get_db)):
    try:
        return crs_crud.create_course(db=db, course=course)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating course: {e}")
    
@router.get("/{course_id}", response_model=Course)
def read_course_route(course_id: int, db: Session = Depends(get_db)):
    db_course = crs_crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.put("/{course_id}", response_model=Course)
def update_course_route(course_id: int, course: Crs_Update, db: Session = Depends(get_db)):
    db_course = crs_crud.update_course(db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course_route(course_id: int, db: Session = Depends(get_db)):
    db_course = crs_crud.delete_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return None