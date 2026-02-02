from typing import Optional
from sqlmodel import SQLModel, Field, UniqueConstraint
from pydantic import EmailStr

class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("email"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(index=True)
    password_hash: str
    role: str = Field(default="user")
    is_active: bool = Field(default=True)
