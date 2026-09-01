from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agent_tool_discount():
    response = client.post("/agent/chat", json={"message": "Can I get a discount?"})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == 80.0
    assert data["confidence"] == "100.0%"

def test_agent_tool_currency():
    response = client.post("/agent/chat", json={"message": "How many rupee is 100 USD?"})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == 8300.0
    assert data["confidence"] == "100.0%"

def test_agent_rag_query():
    response = client.post("/agent/chat", json={"message": "Where is the office located?"})
    assert response.status_code == 200
    data = response.json()
    assert "San Francisco" in data["response"]
    assert "%" in data["confidence"]
