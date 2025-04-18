from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate
from app.models import user as user_model
from app.utils import get_password_hash
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
def get_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    hashed_pw = get_password_hash(password)
    user = user_model.User(name=name, email=email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully!"}
