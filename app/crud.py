from sqlalchemy.orm import Session

from . import models, schemas

from app.utils.hasher import Hasher


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(name = user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user and Hasher.verify_password(password, user.hashed_password):
        return user
    else:
        pass

def update_user(db: Session, db_user: models.User, user: schemas.UserUpdate):
    db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user
