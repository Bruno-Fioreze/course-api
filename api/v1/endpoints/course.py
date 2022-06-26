from typing import List

from fastapi import APIRouter, Query, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models import course as models
from schemas import course as schemas
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Course)
async def post_course(course: schemas.Course, db: AsyncSession = Depends(get_session)):
    course = models.Course(title=course.title, lesson=course.lesson, hour=course.hour)
    db.add(course)
    await db.commit()
    return course


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Course])
async def get_course(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(schemas.Course)
        result = await session.execute(query)
        courses: List[models.Course] = result.scalars().all()
        return courses

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=List[schemas.Course])
async def detail_course(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(models.Course).filter(models.Course.id == id)
        result = await session.execute(query)
        course: List[models.Course] = result.scalar_one_or_none()
        if not course:
            raise HTTPException(detail="Not Found", status=status.HTTP_404_NOT_FOUND)
        return course

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.Course])
async def put_course(id: int, course: schemas.Course, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(models.Course).filter(models.Course.id == id)
        result = await session.execute(query)
        course_result: List[models.Course] = result.scalar_one_or_none()
        if not course:
            raise HTTPException(detail="Not Found", status=status.HTTP_404_NOT_FOUND)
        
        course.title = course_result.title
        course.lesson = course_result.lesson
        course.hour = course_result.hour
        await session.commit()
        return course


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.Course])
async def delete_course(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(models.Course).filter(models.Course.id == id)
        result = await session.execute(query)
        course: List[models.Course] = result.scalar_one_or_none()
        if not course:
            raise HTTPException(detail="Not Found", status=status.HTTP_404_NOT_FOUND)

        await session.delete(course)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)