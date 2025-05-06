from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.utils import jwt
from ..utils.hasher import Hasher
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.dependencies import get_db

router = APIRouter()

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user and Hasher.verify_password(password, user.hashed_password):
        return user

@router.post(
    path="/token",
    response_model=schemas.Token, tags=["Authentication"]
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # find and check password
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # generate token
    access_token_expires = timedelta(minutes=3600)
    access_token = jwt.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post(
    path="/forgot-password",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Authentication"]
)
def forgot_password(
    email: schemas.Email,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, email.email)
    ## TODO: Send email to user

    return {
        "message": "OK. If the user is in our database the email will be send."
    }


@router.post(
    path="/reset-password",
    status_code=status.HTTP_200_OK,
    tags=["Authentication"]
)
def reset_password(
    reset: schemas.ResetPassword,
    db: Session = Depends(get_db)
):
    pass
