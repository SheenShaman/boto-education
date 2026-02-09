from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_shorten():
    result = client.post(
        url="/shorten",
        json={"url": "https://www.google.com"}
    )
    short_url = result.json()["short_url"]

    assert result.status_code == 200
    assert short_url[:-6] == 'http://localhost:8000/'
