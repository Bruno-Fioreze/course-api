from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    
    id: Optional[int]
    title: str
    lesson: int
    hour: int

    class Condig:
        orm_mode = True
