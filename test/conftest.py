import pytest
from app.main import app
from app.db.database import Base
from app.dependencies import get_db
from app import crud, schemas, models
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Default to using sqlite in memory for fast tests.
# Can be overridden by environment variable for testing in CI against other
# database engines
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                           "check_same_thread": False})
    # if not database_exists:
    #     create_database(engine.url)
    Base.metadata.create_all(bind=engine)

    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()

    # begin a non-ORM transaction
    transaction = connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection, autoflush=False)
    # db = Session(db_engine)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c


# USERS FIXTURES
@pytest.fixture
def users(db):
    # Users are create by the crud becouse it hash the password
    users = []
    users.append(crud.create_user(db, schemas.UserCreate(
        email="test@test.cl", password="Test12345", name="Test User")))
    users.append(crud.create_user(db, schemas.UserCreate(
        email="test2@test.cl", password="Test12345", name="Test User")))
    return users

# PROJECTS FIXTURES
@pytest.fixture
def projects(db):
    projects = [
        models.Project(title="Primer proyecto colaborativo",description="El proyecto trata de..."),
        models.Project(title="Segundo proyecto colaborativo", description="El proyecto trata de...")
    ]
    db.add_all(projects)
    db.commit()
    return projects

# ROLES FIXTURES
@pytest.fixture
def roles(db):
    roles = [models.Role(role="project_manager"), models.Role(
        role="developer"), models.Role(role="UX/UI")]
    db.add_all(roles)
    db.commit()
    return roles

# TOKEN FIXTURE
@pytest.fixture(scope="function")
def token(db, users, client):
    credentials = {'username': 'test@test.cl', 'password': 'Test12345'}
    response = client.post("/auth/token", data=credentials)
    return response.json()["access_token"]
