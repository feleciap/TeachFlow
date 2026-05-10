from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post(
    "/",
    response_model=UserRead,
)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    service = UserService(db)

    return await service.get_or_create_user(user_data)