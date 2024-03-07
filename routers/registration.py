import sys

sys.path.append("..")

from typing import Optional
from fastapi import Depends, HTTPException, APIRouter
import server.models as models
from server.database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/registration",
    tags=["registration"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# class Todo(BaseModel):
#     title: str
#     description: Optional[str]
#     priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
#     complete: bool


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Guardian).all()

