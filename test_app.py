import pytest

from main import app as flask_app


TEST_POSTS = [
    {
        "id": 1,
        "title": "Test post",
        "subtitle": "A test subtitle",
        "body": "Test body",
    }
]


class FakeResponse:
    def json(self):
        return TEST_POSTS


@pytest.fixture
def client(monkeypatch):
    flask_app.config.update(TESTING=True)
    monkeypatch.setattr("main.requests.get", lambda *args, **kwargs: FakeResponse())

    with flask_app.test_client() as test_client:
        yield test_client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Test post" in response.data


def test_get_post(client):
    response = client.get("/post/1")

    assert response.status_code == 200
    assert b"Test post" in response.data
    assert b"Test body" in response.data