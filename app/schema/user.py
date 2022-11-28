from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]


class UserResponse(BaseModel):
    username: str
    email: str

    # enable interop between orm and pydantic
    class Config:
        orm_mode = True
