from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base
from app.dependencies import get_db

from sqlalchemy.orm import Session

from app.main import app

def test_app():

    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create database
    Base.metadata.create_all(bind=engine)

    # def override_get_db():
    #     try:
    #         db = TestingSessionLocal()
    #         db.begin()
    #         yield db
    #     finally:
    #         db.rollback()
    #         db.close()

    def override_get_db():
        connection = engine.connect()

        # begin a non-ORM transaction
        transaction = connection.begin()

        # bind an individual Session to the connection
        db = Session(bind=connection)
        # db = Session(engine)

        yield db

        db.rollback()
        connection.close()


    app.dependency_overrides[get_db] = override_get_db

    return app
