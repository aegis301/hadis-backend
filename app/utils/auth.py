from passlib.context import CryptContext

import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

# instantiate CryptContext class
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # should be kept secret
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")  # should be kept secret


def get_hashed_password(password: str) -> str:
    """
    Hashes PWD

    Takes in the plain text password provied and returns a hased version using the specified hashing algorithm

    Parameters
    ----------
    password : str
        Plain text password

    Returns
    -------
    str
        Hased version of the plain text password.
    """
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """
    Verify provided password.

    Takes in the provided password and matches it against hashed password in the database using CryptContext

    Parameters
    ----------
    password : str
        Password provided by the user
    hashed_pass : str
        Hashed password stored in the database

    Returns
    -------
    bool
        Indicator wether verification was successfull
    """
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Creates the access token.

    Parameters
    ----------
    subject : Union[str, Any]
        Payload to be encoded

    expires_delta : int, optional
        Expiration time, by default None

    Returns
    -------
    str
        Access token
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """Same as create_access_token but for refresh token with longer expiration time"""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
