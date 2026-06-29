import requests
import allure

from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    @allure.step('Sending request to get all memes')
    def get_all_memes(self, token):
        self.headers['Authorization'] = token
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()

    # Метод для негативных тестов
    @allure.step('Trying to get all memes with invalid data')
    def try_get_all_memes(self, token):
        self.headers['Authorization'] = token
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.status_code = self.response.status_code

    @allure.step('Checking response body structure')
    def check_response_structure(self):
        data = self.response_body["data"]
        assert data, "Data is missed"
        assert type(data) is list, "Data is not a list"
        for meme in data:
            assert type(meme) is dict, f"Meme {meme}is not a dict"

            assert 'id' in meme, "Missing 'id' field"
            assert 'text' in meme, "Missing 'text' field"
            assert 'url' in meme, "Missing 'url' field"
            assert 'tags' in meme, "Missing 'tags' field"
            assert 'info' in meme, "Missing 'info' field"
            assert 'updated_by' in meme, "Missing 'updated_by' field"

            assert type(meme["text"]) is str, "Text is not a string"
            assert type(meme["url"]) is str, "url is not a string"
            assert type(meme["tags"]) is list, "tags is not an array"
            assert type(meme["info"]) is dict, "info is not an object"
            assert type(meme["updated_by"]) is str, "updated_by is not an string"
