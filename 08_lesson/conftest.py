import pytest
import uuid
from api_client import YougileAPIClient

API_KEY = ""
COMPANY_ID = ""


@pytest.fixture(scope="session")
def api_client():
    return YougileAPIClient(API_KEY)


@pytest.fixture
def test_project_data():
    return {
        "title": f"Test Project {uuid.uuid4().hex[:8]}",
        "companyId": COMPANY_ID,
        "users": {},
        "groups": {}
    }


@pytest.fixture
def created_project(api_client, test_project_data):
    response = api_client.create_project(test_project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    yield project_id
    api_client.delete_project(project_id)
