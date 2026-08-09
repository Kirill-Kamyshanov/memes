import pytest
import requests

from config.environments import Environment, _URLS, EnvironmentConfig, load_environment
from endpoints.get_meme_id import GetOneMemeById
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize_token import CheckAuthorizeToken
from endpoints.get_memes import GetAllMemes
from endpoints.post_meme import PostAMeme
from endpoints.put_meme_id import PutMemeById
from endpoints.delete_meme_id import DeleteMeme


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--env", action="store", default="dev", help='Environment to use')


@pytest.fixture(scope='session')
def env(request: pytest.FixtureRequest) -> Environment | None:
    env_name = request.config.getoption('--env').lower()
    try:
        return Environment(env_name)
    except:
        print(f"Environment '{env_name}' not found")


@pytest.fixture(scope="session")
def env_config(env: Environment) -> EnvironmentConfig:
    config = load_environment(env)
    print(f"\n- Окружение: {env}\n- URL: {config.url}\n")
    return config


@pytest.fixture(scope='session')
def check_token(env_config):
    def new_test_token():
        user = {"name": "Wowa"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{env_config.url}/authorize', json=user, headers=headers)
        auth_token = response.json()['token']
        print(f'\nСгенерирован токен для тестовой сессии: {auth_token}')
        return auth_token

    # По умолчанию используется токен из .env
    token = env_config.token

    # проверка валидности тестового токена. В случае протухания генерация нового и обновление .env
    response = requests.get(f'{env_config.url}/authorize/{token}')
    if response.status_code == 404:
        print(f'Токен {token} устарел. Генерация нового токена...')
        token = new_test_token()
        print("Новый токен:", token)
        with open(".env", "w") as file:
            file.write(f"TOKEN={token}")
        return token
    print(f'\nТокен активен: {"*" * len(token)}. Новая генерация не требуется')
    return token


# Используется только для GET (по id) и PUT
@pytest.fixture()
def create_test_meme_then_delete(check_token, env_config):
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
    meme_id = requests.post(f'{env_config.url}/meme', json=body, headers=headers).json()["id"]
    print(f'\nТестовый мем {meme_id} успешно создан')
    yield meme_id
    requests.delete(f'{env_config.url}/meme/{meme_id}', headers=headers)
    print(f'Тестовый мем {meme_id} успешно удалён')


# фикстуры для создания экземпляров классов (эндпойнтов)

@pytest.fixture()
def post_authorize(env_config):
    return PostAuthorize(env_config.url)


@pytest.fixture()
def get_authorize_token(env_config):
    return CheckAuthorizeToken(env_config.url)


@pytest.fixture()
def get_memes(env_config):
    return GetAllMemes(env_config.url)


@pytest.fixture()
def get_meme_id(env_config):
    return GetOneMemeById(env_config.url)


@pytest.fixture()
def post_meme(env_config):
    return PostAMeme(env_config.url)


@pytest.fixture()
def put_meme_id(env_config):
    return PutMemeById(env_config.url)


@pytest.fixture()
def delete_meme_id(env_config):
    return DeleteMeme(env_config.url)
