from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="Auth API",
    description="Authentication system with FastAPI and PostgreSQL",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Auth API is running"}