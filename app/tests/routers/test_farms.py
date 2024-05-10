from fastapi.testclient import TestClient


def test_read_farms(client: TestClient) -> None:
    response = client.get("/farms")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "crop": "wheat"},
        {"id": 2, "crop": "barley"},
        {"id": 3, "crop": "hops"},
    ]
