import pytest
import requests

from endpoints.get_meme_id import GetOneMemeById
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize_token import CheckAuthorizeToken
from endpoints.get_memes import GetAllMemes
from endpoints.post_meme import PostAMeme
from endpoints.put_meme_id import PutMemeById
from endpoints.delete_meme_id import DeleteMeme

url = 'http://memesapi.course.qa-practice.com'





# фикстура в целом рабочая, но надо будет дооптимизировать потом
@pytest.fixture(scope='session')
def check_token():
    def first_test_token():
        user = {"name": "Wowa"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{url}/authorize', json=user, headers=headers)
        auth_token = response.json()['token']
        print(f'\nСгенерирован токен для тестовой сессии: {auth_token}')
        return auth_token

    # Пока захардкожен валидный токен, чтобы не генерировать зря.
    # При передаче пустой строки будет генерировать новый один раз в сессию
    token = "EcwZL4QkzSzkTrb"


    # генерация токена для тестовой сессии
    if not token:
        token = first_test_token()


    # проверка валидности тестового токена
    response = requests.get(f'{url}/authorize/{token}')
    if response.status_code == 404:
        print(f'Токен {token} устарел. Генерация нового токена...')
        token = first_test_token()
        print("Новый токен:", token)
        return token
    print(f'\nТокен активен: {token}. Новая генерация не требуется')
    return token





# Используется только для GET (по id) и PUT
@pytest.fixture()
def create_test_meme_then_delete(check_token):
    body = {
        "text": "description",
        "url": "https://memes",
        "tags": [
            "first",
            "second"
        ],
        "info": {
            "additional info": "training mem"
        }
    }
    headers = {'Content-Type': 'application/json', 'Authorization': f'{check_token}'}
    meme_id = requests.post(f'{url}/meme', json=body, headers=headers).json()["id"]
    print(f'\nТестовый мем {meme_id} успешно создан')
    yield meme_id
    requests.delete(f'{url}/meme/{meme_id}', headers=headers)
    print(f'Тестовый мем {meme_id} успешно удалён')







# фикстуры для создания экземпляров классов (эндпойнтов)

@pytest.fixture()
def post_authorize():
    return PostAuthorize()

@pytest.fixture()
def get_authorize_token():
    return CheckAuthorizeToken()

@pytest.fixture()
def get_memes():
    return GetAllMemes()

@pytest.fixture()
def get_meme_id():
    return GetOneMemeById()


@pytest.fixture()
def post_meme():
    return PostAMeme()


@pytest.fixture()
def put_meme_id():
    return PutMemeById()


@pytest.fixture()
def delete_meme_id():
    return DeleteMeme()