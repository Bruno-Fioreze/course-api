from core.configs import settings

from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship


class Course(settings.DBBaseModel):

    id:int = Column(Integer, primary_key= True, autoincrement=True)
    title: str = Column(String(100))
    lesson: int = Column(Integer)
    minister: int = Column(Integer, ForeignKey("user.id"))
    creator = relationship(
        "user", back_populates="course", lazy="joined"
    )
    hour: int = Column(Integer)
    __tablename__ = "course"

