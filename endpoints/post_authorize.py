import requests
import allure

from endpoints.endpoint import Endpoint


class PostAuthorize(Endpoint):
    @allure.step('Generation new token')
    def generate_new_token(self, body):
        self.response = requests.post(f'{self.url}/authorize', json=body, headers=self.headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()

    # Метод для негативных тестов
    @allure.step('Trying to generate new token with invalid request body')
    def try_generate_new_token(self, body):
        self.response = requests.post(f'{self.url}/authorize', json=body, headers=self.headers)
        self.status_code = self.response.status_code

    @allure.step('Checking response body structure')
    def check_response_structure(self):
        assert "token" in self.response_body, "Token is missing"
        assert "user" in self.response_body, "User is missing"
        assert type(self.response_body['token']) is str, "Incorrect token type"
        assert type(self.response_body['user']) is str, "Incorrect user type"
