import requests
import allure

from endpoints.endpoint import Endpoint


class CheckAuthorizeToken(Endpoint):
    @allure.step('Test checking valid token')
    def checking_auth_token(self, token, name):
        self.response = requests.get(f'{self.url}/authorize/{token}')
        self.response_body = self.response.text
        self.status_code = self.response.status_code
        assert self.response_body == f'Token is alive. Username is {name}', 'Invalid response body'

    # Метод для негативных тестов
    @allure.step('Test checking invalid token')
    def try_checking_auth_token(self, token):
        self.response = requests.get(f'{self.url}/authorize/{token}')
        self.status_code = self.response.status_code
