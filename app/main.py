from fastapi import FastAPI
from app.routers import auth
from app.database import engine
from app import models

app = FastAPI(
    title="Auth API",
    description="Authentication system with FastAPI and PostgreSQL",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        print("✅ Database connected successfully")

@app.get("/")
async def root():
    return {"message": "Auth API is running"}