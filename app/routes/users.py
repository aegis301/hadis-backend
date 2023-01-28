from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from app.database.models.default import ResponseModel, ErrorResponseModel
from ..database.users import create_single_user, authenticate_user
from ..database.models.auth import UserSchema, TokenSchema


router = APIRouter()

headers = {"Access-Control-Allow-Origin": "*"}


@router.post("/register", response_description="Create new user")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await create_single_user(user)
    return ResponseModel(new_user["username"], "User created successfully.", headers)


@router.post("/login", response_description="Login user", response_model=TokenSchema)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    tokens = await authenticate_user(form_data)
    return tokens
