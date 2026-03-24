import requests
import allure

from endpoints.endpoint import Endpoint


class PostAMeme(Endpoint):
    @allure.step('Creating new meme')
    def create_new_meme(self, token, body):
        self.headers['Authorization'] = token
        response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
        self.status_code = response.status_code
        self.response_body = response.json()
        self.meme_id = response.json()['id']
        self.user = response.json()['updated_by']

    # Метод для негативных тестов
    @allure.step('Trying to create new meme with invalid data')
    def try_create_new_meme(self, token, body):
        self.headers['Authorization'] = token
        response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
        self.status_code = response.status_code

    @allure.step('Deleting test meme')
    def delete_test_meme(self):
        requests.delete(f'{self.url}/meme/{self.meme_id}', headers=self.headers)
        print(f'тестовый мем {self.meme_id} успешно удалён')
