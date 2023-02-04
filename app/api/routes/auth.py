from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api.middleware.db_session import get_db
from app.schema.auth import LoginPayload
from app.schema.user import UserCreate, UserResponse
from app.service import user_service, auth_service

router = APIRouter()


@router.post("/login")
def get_jwt_token(payload: LoginPayload, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, payload)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = auth_service.create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/signup", response_model=UserResponse, status_code=201)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    if not user_service.can_register_user(db, payload):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email address or username taken!",
        )
    return user_service.register_user(db, payload)
