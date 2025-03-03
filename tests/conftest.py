import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def postgres_container():

    with PostgresContainer("postgres:15") as postgres:
        yield postgres

@pytest.fixture(scope="session")
def engine(postgres_container):

    engine = create_engine(postgres_container.get_connection_url())
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db(engine):

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    yield session
    session.rollback()
    session.close()

@pytest.fixture(scope="function")
def client(db):

    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
