from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

from app.utils import jwt
"""
    Role Schemas.
"""
class Role(BaseModel):
    id: int
    role: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "id": 1,
                "role": "developer"
            }
        }

"""
    UserProject
"""
class UserProjectBase(BaseModel):
    user_id: Optional[int]
    project_id: Optional[int]
    role_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "user_id": 1,
                "project_id": 1,
                "role_id": 1
            }
        }

"""
    Project
"""
class ProjectBase(BaseModel):
    title: str = Field(...,min_length=5, max_length=255)
    description: str = Field(...,min_length=10, max_length=255)
    private: Optional[bool]
    active: Optional[bool]
    starts: Optional[int] = 0

    class Config:
        schema_extra = {
            "example":{
                "title": "CuantoMasMejor",
                "description": "Aplicacion web que calcula tus gastos.",
                "private": False,
                "active": True
            }
        }

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
    email: EmailStr
    password: str = Field(...,min_length=8, max_length=255)

    class Config:
        schema_extra = {
            "example":{
                "name": "Andres Chacon",
                "email": "andres.ch@pm.me",
                "password": "Test12345"
            }
        }

class User(UserBase):
    id: int
    email: str = EmailStr(...)
    is_active: bool

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
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

class UserProject(UserProjectBase):
    user: User
    role: Role

class ProjectSchema(Project):
    users: list[UserProject] = []

class UserSchema(User):
    projects: list[UserProjectBase] = []

# For auth
class Email(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    token: str = Field(..., min_length=10, max_length=255)
    password: str = Field(..., min_length=8)

    class Config:
        schema_extra = {
            "example":{
                "token": jwt.create_access_token({}),
                "password": "Test123456789"
            }
        }
