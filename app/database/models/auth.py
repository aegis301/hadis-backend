from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="Username")
    password: str = Field(..., min_length=8, max_length=20, description="Password")

    class Config:
        orm_mode = True


class TokenSchema(BaseModel):
    access_token: str = Field(...)
    refresh_token: str = Field(...)


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
