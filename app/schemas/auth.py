from pydantic import BaseModel


class TelegramAuth(BaseModel):
    telegram_id: int 
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"