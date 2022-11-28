from fastapi.testclient import TestClient
from pytest_mock import MockerFixture
from app.model.user import User


def test_register_success(mocker: MockerFixture, client: TestClient, mock_user: User):
    """
    If both username and email are available, API should return 201 - Created
    """
    test_payload = {
        "username": mock_user.username,
        "password": mock_user.password,
        "email": mock_user.email,
    }
    mocker.patch("app.service.user_service.can_register_user", return_value=True)
    mocker.patch("app.service.auth_service.authenticate_user", return_value=mock_user)
    mocker.patch(
        "app.service.user_service.register_user",
        return_value=User(**test_payload, id="1"),
    )
    response = client.post("/api/auth/signup", json=test_payload)
    assert response.status_code == 201


def test_register_fail(mocker: MockerFixture, client: TestClient):
    """
    If username or email taken, API should yield 409 - Conflict
    """
    test_payload = {
        "username": "john_doe",
        "password": "password",
        "email": "hello@world.com",
    }

    # mock service layer calls
    mocker.patch("app.service.user_service.can_register_user", return_value=False)
    response = client.post("/api/auth/signup", json=test_payload)
    assert response.status_code == 409


def test_login_success(mocker: MockerFixture, client: TestClient, mock_user: User):
    """
    If credentials are valid API should yield 200 - OK,
    and a valid access token
    """
    test_payload = {"username": mock_user.username, "password": mock_user.password}
    mocker.patch("app.service.auth_service.authenticate_user", return_value=mock_user)

    response = client.post("/api/auth/login", json=test_payload)
    assert response.status_code == 200
    # TODO: verify token is valid, not only that it exists
    assert response.json()["access_token"]


def test_login_fail(mocker: MockerFixture, client: TestClient):
    """
    If credentials are invalid API should yield 401 - Unathenticated,
    """
    test_payload = {"username": "john_doe", "password": "password"}
    mocker.patch("app.service.auth_service.authenticate_user", return_value=None)

    response = client.post("/api/auth/login", json=test_payload)
    assert response.status_code == 401
