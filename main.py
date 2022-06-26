from imp import reload
from fastapi import FastAPI

from core.configs import settings
from api.v1.api import router

import uvicorn

app = FastAPI(title="Course API - FastAPI")
app.include_router(router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)