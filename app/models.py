from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base

class Role(Base):
    __tablename__="roles"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(255))

    user_projects = relationship("UserProject", back_populates="role")

class UserProject(Base):
    __tablename__= "user_projects"
    # id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    project_id = Column(ForeignKey('projects.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    project = relationship("Project", back_populates="users")
    user = relationship("User", back_populates="projects")

    role = relationship("Role", back_populates="user_projects")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    projects = relationship("UserProject", back_populates='user', cascade="all, delete-orphan")

class Project(Base):
    __tablename__= "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    private = Column(Boolean, default=True)
    active = Column(Boolean, default=True)
    starts = Column(Integer, default=0)

    users = relationship("UserProject", back_populates='project')
