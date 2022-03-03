from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    events = relationship("UserEvent", back_populates="user")

class Event(Base):
    __tablename__= "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    image = Column(String(255))
    date = Column(DateTime)

    users = relationship("UserEvent", back_populates="event")

class UserEvent(Base):
    __tablename__= "user_events"

    id = Column(Integer, primary_key=True, index=True)
    relation = Column(String(255), nullable=False)
    confirmed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)

    user = relationship("User", back_populates="events" )
    event = relationship("Event", back_populates="users" )
