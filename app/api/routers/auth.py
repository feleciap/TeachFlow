from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token
from app.database.session import get_db
from app.schemas.auth import (TelegramAuth, TokenResponse,)
from app.schemas.user import UserCreate
from app.services.user_service import UserService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/telegram", response_model=TokenResponse,)
async def telegram_auth(
    auth_data: TelegramAuth,
    db: AsyncSession = Depends(get_db),
):
    service = UserService(db)

    user = await service.get_or_create_user(
        UserCreate(
            telegram_id=auth_data.telegram_id,
            username=auth_data.username,
            first_name=auth_data.first_name,
            last_name=auth_data.last_name,
        )
    )

    token = create_access_token(
        {
            "sub": str(user.id),
            "telegram_id": user.telegram_id,
        }
    )

    return TokenResponse(access_token=token,)