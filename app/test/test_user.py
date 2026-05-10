# app/test_user.py

import asyncio

from app.database.session import AsyncSessionLocal
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.database.db import init_db


async def main():
    await init_db()
    async with AsyncSessionLocal() as session:
        service = UserService(session)

        user = await service.get_or_create_user(
            UserCreate(
                telegram_id=123456789,
                username="testuser",
                first_name="Test",
                last_name="User",
            )
        )

        print(user.id)
        print(user.telegram_id)
        print(user.username)


if __name__ == "__main__":
    asyncio.run(main())