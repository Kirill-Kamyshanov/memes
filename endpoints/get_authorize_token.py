from endpoints.endpoint import Endpoint
import requests

class CheckAuthorizeToken(Endpoint):
    def checking_auth_token(self, token, name):
        self.auth_token = token
        self.response = requests.get(f'{self.url}/authorize/{self.auth_token}')
        self.response_body = self.response.text
        self.status_code = self.response.status_code

        assert self.response_body == f'Token is alive. Username is {name}', 'Invalid response body'