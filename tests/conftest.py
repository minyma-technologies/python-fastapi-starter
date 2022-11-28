import pytest
from pytest_mock import MockerFixture
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.model import User


@pytest.fixture
def client(mocker: MockerFixture):
    mock_db = mocker.create_autospec(Session)
    # do not move import stmt
    from app.main import app

    app.dependency_overrides["get_db"] = mock_db
    client = TestClient(app)
    return client


@pytest.fixture
def mock_user():
    return User(
        id="1", username="john_doe", password="password", email="john_doe@acme.com"
    )


@pytest.fixture
def token(mocker: MockerFixture, mock_user: User, client: TestClient):
    mocker.patch("app.service.auth_service.authenticate_user", return_value=mock_user)
    payload = {"password": mock_user.password, "username": mock_user.username}
    response = client.post("/api/auth/login", json=payload)
    token = response.json()["access_token"]
    return token
