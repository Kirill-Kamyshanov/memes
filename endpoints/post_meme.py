import requests

from endpoints.endpoint import Endpoint


class PostAMeme(Endpoint):
    def create_new_meme(self, token, body):
        # print(token)
        # print(body)
        self.auth_token = token
        self.headers['Authorization'] = self.auth_token
        response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
        self.status_code = response.status_code
        self.response_body = response.json()
        self.meme_id = response.json()['id']
        print(self.response_body)
        # print(self.status_code)

    def delete_test_meme(self):
        requests.delete(f'{self.url}/meme/{self.meme_id}', headers=self.headers)
        print(f'тестовый мем {self.meme_id} успешно удалён')