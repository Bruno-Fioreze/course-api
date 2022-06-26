from core.configs import settings
from core.database import engine
import asyncio

async def create_tables() -> None:
    print("Create table in BD")
    import models.__all
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("create Table Success") 

if __name__ == "__main__":
    asyncio.run(
        create_tables()
    )