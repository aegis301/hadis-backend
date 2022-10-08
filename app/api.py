from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.patients import router as PatientRouter

app = FastAPI()

app.include_router(PatientRouter, tags=["Patient"], prefix="/patient")


origins = ["http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}
