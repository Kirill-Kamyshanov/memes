import requests

from endpoints.endpoint import Endpoint

class PutMemeById(Endpoint):
    def put_meme_by_id(self, meme_id, token, body):
        self.auth_token = token
        self.meme_id = meme_id
        self.headers['Authorization'] = self.auth_token
        body['id'] = meme_id
        self.old_response_body = requests.get(f'{self.url}/meme/{self.meme_id}', headers=self.headers).json()
        # print(f'Исходные данные: {self.response_body}')
        response = requests.put(f'{self.url}/meme/{meme_id}',json=body, headers=self.headers)
        self.status_code = response.status_code
        self.response_body = response.json()
        print(f'Обновлённые данные: {self.response_body}')


    # Проверка того, что данные мема действительно обновились
    def check_updating_meme(self):
        self.response_body['id'] = int(self.response_body['id'])
        # print(self.response_body)
        # print(self.old_response_body)
        assert self.response_body != self.old_response_body, 'data was not updated'



    # Отдельный метод, т.к. в ответе этого метода type(id) is str
    def check_meme_id(self):
        assert self.meme_id == int(self.response_body['id']), f'meme_id does not match {self.meme_id}'


    # проверка на наличие и типы обязательных полей для мема.
    # Отдельный метод, т.к. в ответе этого метода type(id) is str
    def check_response_structure(self):
        assert 'id' in self.response_body, 'id is missing'
        assert 'info' in self.response_body, 'info is missing'
        assert 'tags' in self.response_body, 'tags is missing'
        assert 'text' in self.response_body, 'text is missing'
        assert 'url' in self.response_body, 'url is missing'
        assert 'updated_by' in self.response_body, 'updated_by is missing'

        assert type(self.response_body) is dict, 'response_body is not dict'

        assert type(self.response_body['id']) is str, 'id is not str'
        assert type(self.response_body['info']) is dict, 'info is not dict'
        assert type(self.response_body['tags']) is list, 'tags is not list'
        assert type(self.response_body['text']) is str, 'text is not string'
        assert type(self.response_body['url']) is str, 'url is not string'
        assert type(self.response_body['updated_by']) is str, 'updated_by is not string'