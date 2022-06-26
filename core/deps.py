from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

from typing import Generator, Optional 

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from core.database import Session
from core.auth import oauth2_schema
from core.configs import settings
from models.user import User
from schemas.user import Token


async def get_session() -> Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()

async def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_schema)) -> User:
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível autenticar a credencial",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False}
        )
        username: str = payload.get("sub")
        if username:
            raise credential_exception
        token: Token = Token(username=username)
    except JWTError:
        raise credential_exception

    async with db as session:
        query = select(User).filter(User.id==int(token.username))
        result = await session.execute(query)
        user: User = result.scalars().unique().one_or_none()

        if not user:
            raise credential_exception
        
        return user
        