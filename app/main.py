from fastapi import FastAPI

from app.api.routers.users import router as users_router
from app.api.routers.auth import router as auth_router


app = FastAPI(title="TeachFlow API")

app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "status": "OK",
    }