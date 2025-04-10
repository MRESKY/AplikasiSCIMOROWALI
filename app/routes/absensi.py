from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def absen():
    return {"message": "Absen berhasil"}
