import requests
import allure

from endpoints.endpoint import Endpoint


class GetOneMemeById(Endpoint):
    @allure.step('Sending request to get meme by id')
    def get_meme_by_id(self, token, meme_id):
        self.meme_id = meme_id
        self.headers['Authorization'] = token
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)
        self.response_body = self.response.json()
        self.status_code = self.response.status_code

    @allure.step('Trying to get a meme with invalid data')
    def try_get_meme_by_id(self, token, meme_id):
        self.headers['Authorization'] = token
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)
        self.status_code = self.response.status_code
