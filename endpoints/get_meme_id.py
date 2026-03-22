import requests

from endpoints.endpoint import Endpoint


class GetOneMemeById(Endpoint):
    def get_meme_by_id(self, token, meme_id):
        self.meme_id = meme_id
        self.auth_token = token
        self.headers['Authorization'] = self.auth_token
        # print(self.auth_token)
        # print(self.headers)
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)
        self.response_body = self.response.json()
        self.status_code = self.response.status_code
        # print(self.response_body['id'])


    def try_get_meme_by_id(self, token, meme_id):
        self.meme_id = meme_id
        self.auth_token = token
        self.headers['Authorization'] = self.auth_token
        # print(self.auth_token)
        # print(self.headers)
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)
        # self.response_body = self.response.json()
        self.status_code = self.response.status_code
        print(self.status_code)
        # print(self.response_body['id'])
