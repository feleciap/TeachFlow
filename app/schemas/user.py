from pydantic import BaseModel


class UserCreate(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserRead(BaseModel):
    id: int
    telegram_id: int
    username: str | None 
    first_name: str | None 
    last_name: str | None 

    model_config = {
        "from_attributes": True
    }