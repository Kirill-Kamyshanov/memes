import pytest
import requests
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize_token import CheckAuthorizeToken
from endpoints.get_memes import GetAllMemes

url = 'http://memesapi.course.qa-practice.com'
headers = {'Content-Type': 'application/json'}
user = {"name": "Wowa"}


@pytest.fixture(scope='session')
def first_test_token():
    response = requests.post(f'{url}/authorize', json=user, headers=headers)
    auth_token = response.json()['token']
    print(f'\nСгенерирован токен для тестовой сессии: {auth_token}')
    return auth_token


@pytest.fixture()
def check_token(first_test_token):
    response = requests.get(f'{url}/authorize/{first_test_token}')
    if response.status_code == 404:
        print(f'Токен {first_test_token} устарел. Генерация нового токена...')
        response = requests.post(f'{url}/authorize', json=user, headers=headers)
        print("Новый токен:", response.json()['token'])
        return response.json()['token']
    print(f'\nТокен активен: {first_test_token}. Новая генерация не требуется')
    return first_test_token






@pytest.fixture()
def post_authorize():
    return PostAuthorize()

@pytest.fixture()
def get_authorize_token():
    return CheckAuthorizeToken()

@pytest.fixture()
def get_memes():
    return GetAllMemes()