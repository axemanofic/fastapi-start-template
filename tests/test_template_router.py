from fastapi.testclient import TestClient

from src.main import app

client: TestClient = TestClient(app)


def test_ping():
    response = client.get("/template/")
    assert response.status_code == 200 and response.json() == {'response': 200}
