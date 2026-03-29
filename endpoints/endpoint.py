import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    meme_id = None
    response_body = None
    status_code = None
    auth_token = None
    user = None
    headers = {"Content-Type": "application/json"}

    # Проверки на статус-коды
    @allure.step('Checking that status code is 200')
    def check_that_status_code_is_200(self):
        assert self.status_code == 200, f'Status code is not 200: {self.status_code}'

    @allure.step('Checking that status code is 400')
    def check_that_status_code_is_400(self):
        assert self.status_code == 400, f'Status code is not 400: {self.status_code}'

    @allure.step('Checking that status code is 401')
    def check_that_status_code_is_401(self):
        assert self.status_code == 401, f'Status code is not 401: {self.status_code}'

    @allure.step('Checking that status code is 404')
    def check_that_status_code_is_404(self):
        assert self.status_code == 404, f'Status code is not 404: {self.status_code}'

    # Проверка на наличия тела ответа
    @allure.step('Checking response body presence')
    def check_response_body_presence(self):
        assert self.response_body, 'Response body is missing'

    # проверка на наличие и типы обязательных полей для мема (для GET by ID /POST)
    @allure.step('Checking response body structure')
    def check_response_structure(self):
        assert 'id' in self.response_body, 'id is missing'
        assert 'info' in self.response_body, 'info is missing'
        assert 'tags' in self.response_body, 'tags is missing'
        assert 'text' in self.response_body, 'text is missing'
        assert 'url' in self.response_body, 'url is missing'
        assert 'updated_by' in self.response_body, 'updated_by is missing'

        assert type(self.response_body) is dict, 'response_body is not dict'

        assert type(self.response_body['id']) is int, 'id is not int'
        assert type(self.response_body['info']) is dict, 'info is not dict'
        assert type(self.response_body['tags']) is list, 'tags is not list'
        assert type(self.response_body['text']) is str, 'text is not string'
        assert type(self.response_body['url']) is str, 'url is not string'
        assert type(self.response_body['updated_by']) is str, 'updated_by is not string'

    # Проверка того, что id мема в ответе соответствует переданному meme_id
    @allure.step('Validate meme_id')
    def check_meme_id(self):
        assert self.meme_id == self.response_body['id'], f'meme_id does not match {type(self.meme_id)} {type(self.response_body)['id']}'

    # Общий метод для POST и PUT
    @allure.step('Checking response body data')
    def check_response_data(self, body):
        body['id'] = self.meme_id
        body['updated_by'] = self.user
        self.response_body['id'] = int(self.response_body['id'])
        assert body == self.response_body, 'Incorrect response body'

