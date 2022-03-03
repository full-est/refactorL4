from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator


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
    # events: list[Event] = []

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    email: Optional[str]
    password: Optional[str]

#
# """
#     Event Schemas.
# """
# class EventBase(BaseModel):
#     name: str
#     description: str
#     date: datetime
#
# class Event(EventBase):
#     id: int
#     users: list[Event] = []
#
#     class Config:
#         orm_mode = True
#
# """
#     UserEvent Schemas.
# """
# class UserEventBase(BaseModel):
#     relation: str
#     assistance_confirmed: bool
#
#     @validator('relation')
#     def relation_must_be_included(cls, v):
#         if v not in ["organizer", "guest"]:
#             raise ValueError('must be organizer or guest')
#         return v
#
# class UserEvent(UserEventBase):
#     id: int
#     user: User
#     event: Event
#
#     class Config:
#         orm_mode = True

"""
    Token schemas
"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
