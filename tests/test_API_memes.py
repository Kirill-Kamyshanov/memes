# 1 POST /authorize авторизация                      ПОЗ + НЕГ -
# 2 GET /authorize/<token> проверка жив ли токен    ПОЗ + НЕГ -
# 3 GET /meme получение списка всех мемов           ПОЗ - НЕГ -
# 4 GET /meme/<id> Получение одного мема по id      ПОЗ - НЕГ -
# 5 POST /meme Добавление нового мема                ПОЗ - НЕГ -
# 6 /meme/<id> Изменение существующего мема     ПОЗ - НЕГ -
# 7 DELETE /meme/<id> Удаление мема                    ПОЗ - НЕГ -


user = {"name": "Wowa"}
name = user['name']

# чистовик ПОЗ
# def test_post_authorize(first_test_token, post_authorize):
#     post_authorize.generate_new_token(user)
#     post_authorize.check_that_status_code_is_200()
#     post_authorize.check_response_body_presence()
#     post_authorize.check_response_structure()



# чистовик ПОЗ
# def test_get_authorize_token(get_authorize_token, check_token):
#     get_authorize_token.checking_auth_token(check_token, name)
#     get_authorize_token.check_that_status_code_is_200()


def test_get_memes(get_memes, check_token):
    get_memes.get_all_memes(check_token)
    get_memes.check_that_status_code_is_200()
    get_memes.check_response_body_presence()
    # добавить проверки на структуру ответа (сервер не отвечает пока. Нет схемы)