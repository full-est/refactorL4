from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator

"""
    Role Schemas.
"""
class Role(BaseModel):
    id: int
    role: str

"""
    UserProject
"""
class UserProjectBase(BaseModel):
    user_id: int
    project_id: int
    role_id: int

"""
    Project
"""
class ProjectBase(BaseModel):
    title: str
    description: str
    private: bool
    active: bool
    starts: int

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

"""
    User Schemas.
"""
class UserBase(BaseModel):
    name: Optional[str] = None

class UserCreate(UserBase):
    email: str
    password: str

class User(UserBase):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    email: Optional[str]
    password: Optional[str]



"""
    Token schemas
"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


"""
    With relations. Avoid cirular dependencies.
"""

class UserProjectSchema(UserProjectBase):
    project: Project
    user: User
    role: Role

class ProjectSchema(Project):
    users: list[UserProjectBase] = []

class UserSchema(User):
    projects: list[UserProjectBase] = []
