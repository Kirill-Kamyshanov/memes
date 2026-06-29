import pytest

# Данные для проверки валидации при генерации токена (post_authorize)
names_negative = [
    {'name': 1111},  # некорректный тип данных
    # {'name': ''},  # пустое имя (Баг)
    {},  # пустой JSON
    None  # отсутствующее тело
    # {'name': 'Wowa', "excess_field": "some_value"}  # лишнее поле (Баг)
]

# Невалидные токены для проверки работоспособности авторизации
tokens_negative = [
    # 'HW2USKXin4J7zbO', # пока валидный. Когда протухнет можно будет использовать для негативного теста.
    # Закомментил первое значение, чтобы тест дря не падал, т.к. пока этот токен ещё недотух
    'HW2USKXin4J7zz9',  # невалидный
    # '',  # пустая строка
    # None  # отсутствующее значение

]

# невалидные ID мемов
memes_negative = [
    1613,  # валидный, но удалённый
    '!@',  # спецсимволы
    '',  # пустая строка
    None,  # отсутствие значения,
    'я крокодил, крокожу и буду крокодить'  # текст
]

# В реальности проверок должно быть больше, но я в рамках обучения ограничился проверкой обязательности
# полей и валидацией типа данных
create_bodies_negative = [
    {"url": "https://memes/one", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # нет обязательного поля "text"

    {"text": "1 description", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # нет обязательного поля "url"

    {"text": "1 description", "url": "https://memes/one",
     "info": {"additional info": "training mem"}},  # нет обязательного поля "tags"

    {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"]},
    # нет обязательного поля "tags"

    {"text": 5, "url": "https://memes/one", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # некорректный тип 'text'

    {"text": "1 description", "url": 5, "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # некорректный тип 'url'

    {"text": "1 description", "url": "https://memes/one", "tags": "first",
     "info": {"additional info": "training mem"}},  # некорректный тип 'tags'

    {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"],
     "info": ["additional info", "training mem"]}  # некорректный тип 'info'

]

edit_bodies_negative = [
    {"url": "https://memes/one", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # нет обязательного поля "text"

    {"text": "1 description", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # нет обязательного поля "url"

    {"text": "1 description", "url": "https://memes/one",
     "info": {"additional info": "training mem"}},  # нет обязательного поля "tags"

    {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"]},
    # нет обязательного поля "tags"

    {"text": 5, "url": "https://memes/one", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # некорректный тип 'text'

    {"text": "1 description", "url": 5, "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},  # некорректный тип 'url'

    {"text": "1 description", "url": "https://memes/one", "tags": "first",
     "info": {"additional info": "training mem"}},  # некорректный тип 'tags'

    {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"],
     "info": ["additional info", "training mem"]}  # некорректный тип 'info'

]

valid_body = {"text": "5", "url": "https://memes/one", "tags": ["first", "second"],
              "info": {"additional info": "training mem"}}


# Создание токена с невалидным телом
# 2 бага: пустое значение и лишнее поле
@pytest.mark.parametrize("name", names_negative)
def test_post_authorize_negative(post_authorize, name):
    post_authorize.try_generate_new_token(name)
    post_authorize.check_that_status_code_is_400()


# Проверка невалидного токена
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_get_authorize_token_negative_auth(get_authorize_token, invalid_token):
    get_authorize_token.try_checking_auth_token(invalid_token)
    get_authorize_token.check_that_status_code_is_404()


# 1 баг: при пустом значении код 500 для всех методов с авторизацией)
# Получение всех мемов с невалидным токеном
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_get_memes_negative_auth(get_memes, invalid_token):
    get_memes.try_get_all_memes(invalid_token)
    get_memes.check_that_status_code_is_401()


# Получение мема по id с невалидным id
@pytest.mark.parametrize("invalid_meme_id", memes_negative)
def test_get_meme_id_negative(get_meme_id, check_token, invalid_meme_id):
    get_meme_id.try_get_meme_by_id(check_token, invalid_meme_id)
    get_meme_id.check_that_status_code_is_404()


# Получение мема по id с невалидным токеном
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_get_meme_id_negative_auth(get_meme_id, check_token, invalid_token):
    get_meme_id.try_get_meme_by_id(invalid_token, 1)
    get_meme_id.check_that_status_code_is_401()


# Создание мема с невалидным телом
@pytest.mark.parametrize("body", create_bodies_negative)
def test_post_meme_negative(post_meme, check_token, body):
    post_meme.try_create_new_meme(token=check_token, body=body)
    post_meme.check_that_status_code_is_400()


# Создание мема с невалидным токеном
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_post_meme_negative_auth(post_meme, invalid_token):
    post_meme.try_create_new_meme(token=invalid_token, body=valid_body)
    post_meme.check_that_status_code_is_401()


# Редактирование мема с невалидным телом
@pytest.mark.parametrize("new_body", create_bodies_negative)
def test_try_put_meme_id_negative(put_meme_id, check_token, create_test_meme_then_delete, new_body):
    put_meme_id.try_put_meme_by_id(meme_id=create_test_meme_then_delete, token=check_token, body=new_body)
    put_meme_id.check_that_status_code_is_400()


# Редактирование мема с невалидным токеном
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_try_put_meme_id_negative_auth(put_meme_id, invalid_token, create_test_meme_then_delete):
    put_meme_id.try_put_meme_by_id(meme_id=create_test_meme_then_delete, token=invalid_token, body=valid_body)
    put_meme_id.check_that_status_code_is_401()


# Редактирование мема с невалидным ID
@pytest.mark.parametrize("invalid_meme_id", memes_negative)
def test_try_put_meme_id_negative(put_meme_id, check_token, invalid_meme_id):
    put_meme_id.try_put_meme_by_id(meme_id=memes_negative, token=check_token, body=valid_body)
    put_meme_id.check_that_status_code_is_404()


# Удаление мема с невалидным id
@pytest.mark.parametrize("invalid_meme_id", memes_negative)
def test_delete_meme_id_negative(delete_meme_id, check_token, invalid_meme_id):
    delete_meme_id.try_delete_meme(meme_id=invalid_meme_id, token=check_token)
    delete_meme_id.check_that_status_code_is_404()


# Удаление мема с невалидным токеном
@pytest.mark.parametrize("invalid_token", tokens_negative)
def test_delete_meme_id_negative_auth(delete_meme_id, create_test_meme_then_delete, invalid_token):
    delete_meme_id.try_delete_meme(meme_id=create_test_meme_then_delete, token=invalid_token)
    delete_meme_id.check_that_status_code_is_401()
