from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.api.dependencies.auth import (get_current_user)
from app.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("/",response_model=UserRead,)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    service = UserService(db)

    return await service.get_or_create_user(user_data)

@router.get("/me", response_model=UserRead,)
async def get_me(
    current_user: User = Depends(
        get_current_user
    ),
):
    return current_user