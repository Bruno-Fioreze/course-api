from fastapi import APIRouter

from api.v1.endpoints import course

router = APIRouter()
router.include_router(course, prefix="/course", tags=["courses"])
