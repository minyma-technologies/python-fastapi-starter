from fastapi import APIRouter
from app.api.routes import auth, user

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(user.router, prefix="/user")


@router.get("/")
def status():
    return {"status": "running"}
