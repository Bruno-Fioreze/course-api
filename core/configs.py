from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
        Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
    DBBaseModel = declarative_base()

    JWT_SECRET: str = "1-Y9JTNtBRULwHML8xf45RE6LjU7lHgHCZDmyyGQt1Q"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()