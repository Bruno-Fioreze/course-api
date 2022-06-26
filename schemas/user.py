from typing import Optional, List
from pydantic import BaseModel, EmailStr

from schemas.course import Course

class Token(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: EmailStr
    is_admin: bool = False
 
    class Config:
        orm_mode = True

class UserCreate(User):
    password: str

class UserCourse(User):
    course: Optional[List[Course]]

class UserCreate(User):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    is_admin: Optional[bool]

