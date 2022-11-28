from fastapi.testclient import TestClient
from pytest_mock import MockerFixture
from app.model.user import User


def test_user_update_success(
    mocker: MockerFixture, token: str, mock_user: User, client: TestClient
):
    """
    If credentials and payload are valid API should yield 200 - OK
    """
    test_payload = {
        "username": "john_doe",
        "password": "password",
        "email": "hello@world.com",
    }
    mocker.patch("app.service.user_service.update_user", return_value=mock_user)
    mocker.patch("app.repo.user_repo.get", return_value=mock_user)
    response = client.put(
        "/api/user", json=test_payload, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200


def test_user_update_fail_invalid_credentials(client: TestClient):
    """
    If credentials are invalid, API should yield 401
    """
    test_payload = {
        "username": "john_doe",
        "password": "password",
        "email": "hello@world.com",
    }
    response = client.put(
        "/api/user",
        json=test_payload,
        headers={"Authorization": f"Bearer bad.token.xyz"},
    )
    assert response.status_code == 401


def test_user_update_fail_invalid_payload(
    mocker: MockerFixture, client: TestClient, token: str, mock_user: User
):
    """
    If payload is invalid, API should yield 400
    """
    test_payload = {
        "wrong_field": "john_doe",
    }
    mocker.patch("app.service.user_service.update_user", return_value=mock_user)
    mocker.patch("app.repo.user_repo.get", return_value=mock_user)

    response = client.put(
        "/api/user", json=test_payload, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
