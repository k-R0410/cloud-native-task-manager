
import pytest
import app.app as app_module

app = app_module.app


@pytest.fixture
def client():
    # Reset task data before every test
    app_module.tasks.clear()
    app_module.next_id = 1
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client

    # Clean up after every test
    app_module.tasks.clear()
    app_module.next_id = 1


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_tasks(client):
    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert response.json == []


def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"title": "Learn GitHub Actions"}
    )

    assert response.status_code == 201
    assert response.json["title"] == "Learn GitHub Actions"
    assert response.json["completed"] is False


def test_create_task_without_title(client):
    response = client.post(
        "/api/tasks",
        json={}
    )

    assert response.status_code == 400


def test_update_task(client):
    created = client.post(
        "/api/tasks",
        json={"title": "Learn Docker"}
    )

    task_id = created.json["id"]

    response = client.patch(
        f"/api/tasks/{task_id}",
        json={"completed": True}
    )

    assert response.status_code == 200
    assert response.json["completed"] is True


def test_delete_task(client):
    created = client.post(
        "/api/tasks",
        json={"title": "Learn Kubernetes"}
    )

    task_id = created.json["id"]

    response = client.delete(
        f"/api/tasks/{task_id}"
    )

    assert response.status_code == 200
    assert response.json["message"] == "Task deleted"
