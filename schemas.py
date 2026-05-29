from pydantic import BaseModel, Field
from typing import Optional

class StudentCreate(BaseModel):
    student_name: str = Field(min_length=2)
    email: str
    department: str

class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None

class CourseCreate(BaseModel):
    course_name: str
    course_code: str

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_code: Optional[str] = None

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
