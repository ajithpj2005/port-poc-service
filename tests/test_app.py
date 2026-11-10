from src.app import app


def test_health():
    resp = app.test_client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_hello():
    resp = app.test_client().get("/hello/port")
    assert resp.get_json() == {"message": "Hello, port!"}
