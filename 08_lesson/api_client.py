import requests
from config import BASE_URL, HEADERS


class YougileAPIClient:
    def __init__(self, token: str):
        self.base_url = BASE_URL
        self.headers = HEADERS.copy()
        self.headers["Authorization"] = f"Bearer {token}"

    def create_project(self, data: dict):
        """Создание нового проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def get_project(self, project_id: str):
        """Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id: str, data: dict):
        """Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def delete_project(self, project_id: str):
        """Архивация проекта (имитация удаления)"""
        archive_data = {"archived": True}
        return self.update_project(project_id, archive_data)
