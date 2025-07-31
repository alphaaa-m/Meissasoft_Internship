from pydantic import BaseModel
from typing import Optional, List

class Crs_Base(BaseModel):
    crs_title: str
    crs_code: str 
    tchr_id: int
    department: Optional[str] = None


class Crs_Create(Crs_Base):
    pass

class Crs_Update(BaseModel):
    crs_title: Optional[str] = None
    crs_code: Optional[str] = None
    tchr_id: Optional[int] = None
    department: Optional[str] = None

class Course(Crs_Base):
    crs_id: int

    class Config:
        from_attributes = True
