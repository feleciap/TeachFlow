# app/test_db.py

import asyncio
from sqlalchemy import text

from app.database.db import engine


async def test_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(result.scalar())


if __name__ == "__main__":
    asyncio.run(test_connection())