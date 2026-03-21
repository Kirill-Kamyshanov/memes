import requests

class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    headers = {'Content-Type': 'application/json'}
    meme_id = None
    response_body = None
    status_code = None
    auth_token = None
    user = None








    # Проверки на статус-коды
    def check_that_status_code_is_200(self):
        assert self.status_code == 200, f'Status code is not 200: {self.status_code}'

    def check_that_status_code_is_400(self):
        assert self.status_code == 400, f'Status code is not 400: {self.status_code}'

    def check_that_status_code_is_404(self):
        assert self.status_code == 404, f'Status code is not 404: {self.status_code}'


    # Проверка на наличия тела ответа
    def check_response_body_presence(self):
        assert self.response_body, 'Response body is missing'

