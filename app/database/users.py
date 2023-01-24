from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
import motor.motor_asyncio
from .models.auth import UserSchema
from ..utils.auth import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password,
)


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.hadis

users_collection = database.get_collection("user")


async def create_single_user(data: dict):
    # querying database to check if user already exist
    user = await users_collection.find_one(data["username"], None)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )
    user = {
        "username": data["username"],
        "password": get_hashed_password(data["password"]),
    }
    created_user = await users_collection.insert_one(user)  # saving user to database
    new_user = await users_collection.find_one({"_id": created_user.inserted_id})
    return new_user


async def authenticate_user(form_data):
    user = await users_collection.find_one(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials",
        )
    hashed_password = user["password"]
    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password",
        )

    return {
        "access_token": create_access_token(data={"sub": user["username"]}),
        "refresh_token": create_refresh_token(data={"sub": user["username"]}),
    }
