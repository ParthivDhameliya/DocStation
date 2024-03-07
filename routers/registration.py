import sys

sys.path.append("../server")

from fastapi import Depends, APIRouter, Request
import models as models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/registration",
    tags=["registration"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def registration_form(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def registration(request: Request):
    pass



