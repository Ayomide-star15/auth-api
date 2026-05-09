from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid

# ─── REQUEST SCHEMAS (what the user sends to your API) ───────────────────────

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# ─── RESPONSE SCHEMAS (what your API sends back) ─────────────────────────────

class UserResponse(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    phone_number: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse

class MessageResponse(BaseModel):
    message: str