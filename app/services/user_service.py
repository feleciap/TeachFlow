from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def get_or_create_user(self, user_data: UserCreate,) -> User:
        user = await self.repository.get_by_telegram_id(user_data.telegram_id)

        if user:
            return user
        
        return await self.repository.create(user_data)