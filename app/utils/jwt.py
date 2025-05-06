from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from dotenv import load_dotenv
import os

## TODO: Include this variables on env
# to get a string like this run:
# openssl rand -hex 32

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
