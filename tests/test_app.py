import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import app, projects


def setup_function():
    projects.clear()
    projects.extend([
        {
            "id": 1,
            "name": "테스트 프로젝트",
            "description": "테스트 설명",
            "status": "대기"
        }
    ])


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "테스트 프로젝트".encode() in response.data


def test_add_project():
    client = app.test_client()
    response = client.post("/add", data={
        "name": "새 프로젝트",
        "description": "프로젝트 설명"
    })
    assert response.status_code == 302
    assert len(projects) == 2


def test_edit_project():
    client = app.test_client()
    response = client.post("/edit/1", data={"status": "완료"})
    assert response.status_code == 302
    assert projects[0]["status"] == "완료"


def test_delete_project():
    client = app.test_client()
    response = client.post("/delete/1")
    assert response.status_code == 302
    assert len(projects) == 0
