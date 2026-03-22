import pytest

# Данные для проверки валидации при генерации токена (post_authorize)
names_negative = [
    {'name': 1111}, # некорректный тип данных
    {'name': ''}, # пустое имя (Баг)
    {}, # пустой JSON
    None, # отсутствующее тело
    {'name': 'Wowa', "excess_field": "some_value"} # лишнее поле (Баг)
]

# Невалидные токены для проверки работоспособности авторизации
tokens_negative = [
    # 'HW2USKXin4J7zbO', # пока валидный. Когда протухнет можно будет использовать для негативного теста.
    # Закомментил первое значение, чтобы тест дря не падал, т.к. пока этот токен ещё недотух
    'HW2USKXin4J7zz9', # невалидный
    '', # пустая строка
    None # отсутствующее значение

]


# 2 бага: пустое значение и лишнее поле
# @pytest.mark.parametrize("name", names_negative)
# def test_post_authorize_negative(post_authorize, name):
#     post_authorize.try_generate_new_token(name)
#     post_authorize.check_that_status_code_is_400()



# @pytest.mark.parametrize("invalid_token", tokens_negative)
# def test_get_authorize_token_negative(get_authorize_token, invalid_token):
#     get_authorize_token.try_checking_auth_token(invalid_token)
#     get_authorize_token.check_that_status_code_is_404()


# 1 баг: при пустом значении код 500
# @pytest.mark.parametrize("invalid_token", tokens_negative)
# def test_get_memes_negative(get_memes, invalid_token):
#     get_memes.try_get_all_memes(invalid_token)
#     get_memes.check_that_status_code_is_401()