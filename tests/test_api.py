from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "HackSmith" in response.json()["message"]

def test_ask():
    response = client.post("/ask", json={"query": "What is Nmap?"})
    assert response.status_code == 200
    assert "Received your query" in response.json()["answer"]
