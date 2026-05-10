from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int,) -> User | None:
        stmt = select(User).where(User.telegram_id == telegram_id)

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
    
    async def create(self, user_data: UserCreate,) -> User:
        user = User(
            telegram_id=user_data.telegram_id,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )

        self.session.add(user)

        await self.session.commit()
        await self.session.refresh(user)

        return user
