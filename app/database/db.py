from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker, create_async_engine)

from app.core.config import settings
from app.database.base import Base
from app.models.user import User


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
    )

AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)