from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    full_name: str = Field(...)
    is_active: bool = Field(...)

    class Config:
        orm_mode = True
