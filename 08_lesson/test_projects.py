import os


def test_create_project_positive(api_client, test_project_data):
    response = api_client.create_project(test_project_data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_missing_title(api_client):
    company_id = os.getenv("YOUGILE_COMPANY_ID")
    invalid_data = {
        "companyId": company_id,
        "users": {},
        "groups": {}
    }
    response = api_client.create_project(invalid_data)
    assert response.status_code == 400


def test_get_project_positive(api_client, created_project):
    response = api_client.get_project(created_project)
    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative_not_found(api_client):
    response = api_client.get_project("fake-id-12345")
    assert response.status_code == 404


def test_update_project_positive(api_client, created_project):
    company_id = os.getenv("YOUGILE_COMPANY_ID")
    new_title = "Updated Project"
    update_data = {
        "title": new_title,
        "companyId": company_id
    }
    response = api_client.update_project(created_project, update_data)
    assert response.status_code == 200

    get_response = api_client.get_project(created_project)
    assert get_response.json()["title"] == new_title


def test_update_project_negative_invalid_id(api_client):
    company_id = os.getenv("YOUGILE_COMPANY_ID")
    update_data = {
        "title": "New Title",
        "companyId": company_id
    }
    response = api_client.update_project("invalid_id", update_data)
    assert response.status_code in [400, 404]
