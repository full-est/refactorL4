from sqlalchemy import or_
from sqlalchemy.orm import Session
from . import models, schemas

from app.utils.hasher import Hasher


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(name=user.name, email=user.email,
                          hashed_password=hashed_password)
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


def update_user(db: Session, current_user: models.User, user: schemas.UserUpdate):
    user_dict = user.dict(exclude_unset=True)
    # Replace the password for hashed password on the dict
    if user.password is not None:
        user_dict["hashed_password"] = user_dict.pop("password")
        user_dict["hashed_password"] = Hasher.get_password_hash(user.password)

    db.query(models.User).filter(models.User.id == current_user.id).update(
        user_dict, synchronize_session=False)
    db.commit()
    db.refresh(current_user)
    return current_user


def create_project(db: Session, current_user: models.User, project: schemas.ProjectBase):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    user_project = models.UserProject(
        role=db.query(models.Role).first(),
        user=current_user)
    db_project.users.append(user_project)
    db.commit()
    return db_project


def show_project(db: Session, current_user: models.User, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def show_projects(db: Session, current_user: models.User, skip: int = 0, limit: int = 100, q: str = "%"):
    return db.query(models.Project).filter(or_(models.Project.title.like("%" + q + "%"), models.Project.description.like("%" + q + "%"))).offset(skip).limit(limit).all()
