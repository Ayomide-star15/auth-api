import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID, INET
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name    = Column(String(100), nullable=False)
    last_name     = Column(String(100), nullable=False)
    email         = Column(String(255), nullable=False, unique=True)
    phone_number  = Column(String(20), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    status        = Column(String(20), nullable=False, server_default='active')
    last_login_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at    = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    updated_at    = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))


class Session(Base):
    __tablename__ = "sessions"

    id                 = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id            = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    refresh_token_hash = Column(String(255), nullable=False, unique=True)
    user_agent         = Column(String, nullable=True)
    ip_address         = Column(INET, nullable=False)
    is_invalidated     = Column(Boolean, nullable=False, default=False)
    expires_at         = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at         = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id    = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id", ondelete="SET NULL"), nullable=True)
    action     = Column(String(100), nullable=False)
    ip_address = Column(INET, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))


class LoginAttempt(Base):
    __tablename__ = "login_attempts"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id        = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    ip_address     = Column(INET, nullable=False)
    success        = Column(Boolean, nullable=False, default=False)
    failure_reason = Column(String(100), nullable=True)
    attempted_at   = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))


class TrustedIP(Base):
    __tablename__ = "trusted_ips"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id    = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    ip_address = Column(INET, nullable=False)
    label      = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))