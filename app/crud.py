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

def delete_user(db: Session, current_user: models.User):
    db.delete(current_user)
    db.commit()
    return True

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

def update_project(db:Session, current_user: models.User, project_id: int, project: schemas.ProjectBase ):
    return None

def show_project(db: Session, current_user: models.User, project_id: int):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    # Check if project is not private for show and if it is private only the related users can see it
    if project is not None and not project.private:
        return project
    elif project is not None and db.query(models.UserProject).where(models.UserProject.project_id == project_id, models.UserProject.user_id == current_user.id).first() is not None :
        return project
    else:
        return None

def show_projects(db: Session, current_user: models.User, skip: int = 0, limit: int = 100, q: str = "%"):
    # Here we need check if the project is private, if it is private we need to check if exist relation with the user
    return db.query(models.Project).join(models.UserProject, isouter=True).filter(models.UserProject.user_id == current_user.id, or_(models.Project.title.like("%" + q + "%"), models.Project.description.like("%" + q + "%"))).offset(skip).limit(limit).all()
