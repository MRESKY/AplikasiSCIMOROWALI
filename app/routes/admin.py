from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {"message": "Dashboard admin"}
