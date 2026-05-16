from fastapi import FastAPI

from app.api.routers.users import router as users_router
from app.api.routers.auth import router as auth_router
from app.api.dependencies.logging import (logging_middleware,)
from app.core.config import settings
from app.core.exceptions import (global_exception_handler,)
from app.database.db import init_db


app = FastAPI(title="TeachFlow API")


app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler,)

app.include_router(users_router)
app.include_router(auth_router)


@app.on_event("startup")
async def startup():
    await init_db()

    
@app.get("/")
async def root():
    return {
        "status": "OK",
    }