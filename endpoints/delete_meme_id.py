import requests
from endpoints.endpoint import Endpoint

class DeleteMeme(Endpoint):

    # Для этого эндпойнта создание тестового мема переопределено, т.к. удалять в фикстуре его не нужно
    def create_test_meme(self, token):
        self.auth_token = token
        self.headers['Authorization'] = self.auth_token
        body = {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"],
                "info": {"additional info": "training mem"}}
        # print(self.headers)
        self.meme_id = requests.post(f'{self.url}/meme', json=body, headers=self.headers).json()["id"]
        # print(self.meme_id)


    def delete_meme(self):
        self.response = requests.delete(f'{self.url}/meme/{self.meme_id}',headers=self.headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.text
        print(f'Мем {self.meme_id} удалён')
        assert self.response_body == f'Meme with id {self.meme_id} successfully deleted', 'invalid body'

    def try_delete_meme(self, meme_id, token):
        self.headers['Authorization'] = token
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=self.headers)
        self.status_code = self.response.status_code
        print(self.status_code)


    def check_that_meme_has_been_deleted(self):
        self.response = requests.get(f'{self.url}/meme/{self.meme_id}',headers=self.headers)
        assert self.response.status_code == 404, f'meme has not been deleted {self.response.status_code}'