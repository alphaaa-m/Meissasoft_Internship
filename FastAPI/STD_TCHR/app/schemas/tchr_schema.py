from pydantic import BaseModel, EmailStr
from typing import Optional, List

class Tchr_Base(BaseModel):
    tchr_name: str
    tchr_email: EmailStr
    department: str

class Tchr_Create(Tchr_Base):
    pass

class Tchr_Update(BaseModel):
    tchr_name: Optional[str] = None
    tchr_email: Optional[EmailStr] = None
    department: Optional[str] = None

class Teacher(Tchr_Base):
    tchr_id: int

    class Config:
        from_attributes = True