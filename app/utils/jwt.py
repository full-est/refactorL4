from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

## TODO: Include this variables on env
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "2573f34ad4b5a5f0dfa67ff4c4085fb9f8563decaedcb0e209b4613962089190"
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
