import requests
import allure

from endpoints.endpoint import Endpoint


class PutMemeById(Endpoint):
    @allure.step('Edit meme data by id')
    def put_meme_by_id(self, meme_id, token, body):
        self.meme_id = meme_id
        self.headers['Authorization'] = token
        # Строка ниже нужна для того чтобы можно было использовать одни данные для POST и PUT методов
        body['id'] = self.meme_id
        self.old_response_body = requests.get(f'{self.url}/meme/{self.meme_id}', headers=self.headers).json()
        response = requests.put(f'{self.url}/meme/{self.meme_id}', json=body, headers=self.headers)
        self.status_code = response.status_code
        self.response_body = response.json()
        self.user = self.response_body['updated_by']
        print(f'Обновлённые данные: {self.response_body}')

    @allure.step('Trying to edit meme with invalid data')
    def try_put_meme_by_id(self, meme_id, token, body):
        self.headers['Authorization'] = token
        if meme_id:
            body['id'] = meme_id
        response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=self.headers)
        self.status_code = response.status_code


    # Отдельный метод, т.к. в ответе этого метода type(id) is str
    @allure.step('Validate meme_id')
    def check_meme_id(self):
        assert self.meme_id == int(self.response_body['id']), f'meme_id does not match {self.meme_id}'

    # проверка на наличие и типы обязательных полей для мема.
    # Отдельный метод, т.к. в ответе этого метода type(id) is str
    @allure.step('Checking response body structure')
    def check_response_structure(self):
        assert type(self.response_body) is dict, 'response_body is not dict'

        assert 'id' in self.response_body, 'id is missing'
        assert 'info' in self.response_body, 'info is missing'
        assert 'tags' in self.response_body, 'tags is missing'
        assert 'text' in self.response_body, 'text is missing'
        assert 'url' in self.response_body, 'url is missing'
        assert 'updated_by' in self.response_body, 'updated_by is missing'

        assert type(self.response_body['id']) is str, 'id is not str'
        assert type(self.response_body['info']) is dict, 'info is not dict'
        assert type(self.response_body['tags']) is list, 'tags is not list'
        assert type(self.response_body['text']) is str, 'text is not string'
        assert type(self.response_body['url']) is str, 'url is not string'
        assert type(self.response_body['updated_by']) is str, 'updated_by is not string'
