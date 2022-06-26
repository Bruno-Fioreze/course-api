from cgitb import reset
import token
from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from models.user import User
from core.configs import settings
from core.security import check_pass


from pydantic import EmailStr 

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/user/login"
)

async def auth(email: EmailStr, password:str, db: AsyncSession) -> Optional[User]:
    async with db as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)
        user: User = result.scalars().unique().one_or_none()

        if not user:
            return None
        
        if not check_pass(password, user.password):
            return None
        
        return user

def _create_token(type_token: str, life_time: timedelta, sub: str) -> str:
    payload = {}
    tmz = timezone("America/Sao_paulo")
    expire = datetime.now(tz=tmz) + life_time
    payload.update(
        {"type": type_token, "exp": expire, "iat": datetime.now(tz=tmz), "sub": sub}
    )
        
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM) 

def create_token_access(sub: str) -> str:

    return _create_token(
        type_token="access_token",
        life_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub

    )