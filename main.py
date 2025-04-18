from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import os

from app.routes import user, absensi, admin
from app.database import Base, engine

# Inisialisasi DB
Base.metadata.create_all(bind=engine)

# Inisialisasi FastAPI
app = FastAPI(
    title="Aplikasi Absensi",
    description="Sistem absensi dengan foto dan panel admin",
    version="1.0.0"
)

# Mount static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(BASE_DIR, "app", "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Jinja2 template
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "app", "templates"))


# Routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(absensi.router, prefix="/absen", tags=["Absensi"])
app.include_router(admin.router, tags=["Admin"])

# Halaman utama (login)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Jalankan aplikasi jika file ini dieksekusi langsung
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
