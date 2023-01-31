from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi_login import LoginManager
from .routes.patients import router as PatientRouter
from .routes.users import router as UserRouter
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

SECRET = os.getenv("JWT_SECRET_KEY")
manager = LoginManager(SECRET, "/user/login", use_cookie=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(PatientRouter, tags=["Patient"], prefix="/patient")
app.include_router(UserRouter, tags=["User"], prefix="/user")


origins = ["http://localhost:3000", "localhost:3000", "https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}
