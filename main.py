from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import user, absensi, admin
import uvicorn

app = FastAPI(
    title="Aplikasi Absensi",
    description="Sistem absensi dengan foto dan panel admin",
    version="1.0.0"
)

# Mount static files (foto, css)
app.mount("/static", StaticFiles(directory=r"C:\Users\ARLuser\Documents\Aplikasi SCI MOROWALI\app\static"), name="static")

# Load Jinja2 template
templates = Jinja2Templates(directory="app/templates")

# Include routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(absensi.router, prefix="/absen", tags=["Absensi"])
app.include_router(admin.router, tags=["Admin"])

# Jalankan dengan: uvicorn app.main:app --reload
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
