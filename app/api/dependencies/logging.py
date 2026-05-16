import time
from fastapi import Request

from app.core.logger import logger


async def logging_middleware(request: Request, call_next,):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time:.4f}s"
    )

    return response