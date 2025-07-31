from pydantic import BaseModel, EmailStr
from typing import Optional

class Std_Create(BaseModel):
    std_name: str
    std_email: EmailStr
    department: str

class Std_Update(BaseModel):
    std_name: Optional[str] = None
    std_email: Optional[EmailStr] = None
    department: Optional[str] = None

class Student(Std_Create):
    std_id: int

    class Config:
        from_attributes = True