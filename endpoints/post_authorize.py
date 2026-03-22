from endpoints.endpoint import Endpoint
import requests

class PostAuthorize(Endpoint):
    def generate_new_token(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize', json=body, headers=headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        self.auth_token = self.response_body['token']
        self.user = self.response_body['user']

    # Метод для негативных тестов
    def try_generate_new_token(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize', json=body, headers=headers)
        self.status_code = self.response.status_code
        # print(self.response.text)
        # self.response_body = self.response.text

        # отладка
        # print(self.response_body)
        # print(self.status_code)
        # print(self.auth_token)
        # print(self.user)

    def check_response_structure(self):
        assert "token" in self.response_body, "Token is missing"
        assert "user" in self.response_body, "User is missing"
        assert type(self.response_body["token"]) is str, "Incorrect token type"
        assert type(self.response_body["user"]) is str, "Incorrect user type"