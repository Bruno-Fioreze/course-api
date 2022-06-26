import email
from email.policy import default
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from core.configs import settings

class User(settings.DBBaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
    password = Column(String(256), nullable=True)
    course = relationship(
        "course",
        cascade="all,delete-orphan",
        back_populates="creator",
        uselist=True,
        lazy="joined"
    )