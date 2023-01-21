from passlib.context import CryptContext

import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

# instantiate CryptContext class
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
