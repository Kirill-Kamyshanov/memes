from endpoints.endpoint import Endpoint
import requests

class GetAllMemes(Endpoint):
    def get_all_memes(self, token):
        self.auth_token = token
        self.headers['Authorization'] = self.auth_token

        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()

        print(self.response)
        print(self.status_code)
        print(self.response_body)

    def check_response_structure(self):
        data = self.response_body["data"]
        assert data, "Data is missed"
        assert type(data) is list, "Data is not a list"
        for meme in data:
            # проверка для каждого мема соответствует общей в род. классе
            assert type(meme) is dict, f"Meme {meme}is not a dict"

            assert 'id' in meme, "Missing 'id' field"
            assert 'text' in meme, "Missing 'text' field"
            assert 'url' in meme, "Missing 'url' field"
            assert 'tags' in meme, "Missing 'tags' field"
            assert 'info' in meme, "Missing 'info' field"
            assert 'updated_by' in meme, "Missing 'updated_by' field"

            assert type(meme["id"]) is int, "id is not an integer"
            assert type(meme["text"]) is str, "Text is not a string"
            assert type(meme["url"]) is str, "url is not a string"
            assert type(meme["tags"]) is list, "tags is not an array"
            assert type(meme["info"]) is dict, "info is not an object"
            assert type(meme["updated_by"]) is str, "updated_by is not an string"
