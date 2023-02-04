from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.middleware.db_session import get_db
from app.api.middleware.auth import get_current_user
from app.model.user import User
from app.service import user_service
from app.schema.user import UserUpdate, UserResponse

router = APIRouter()


@router.put("/", response_model=UserResponse)
def update_user(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    updated_user = user_service.update_user(db, user, payload)
    if not updated_user:
        raise HTTPException(status_code=400)
    return updated_user
