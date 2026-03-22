# 1 POST /authorize авторизация                        ПОЗ + НЕГ -
# 2 GET /authorize/<token> проверка жив ли токен       ПОЗ + НЕГ -
# 3 GET /meme получение списка всех мемов              ПОЗ + НЕГ -
# 4 GET /meme/<id> Получение одного мема по id         ПОЗ + НЕГ -
# 5 POST /meme Добавление нового мема                  ПОЗ + НЕГ -
# 6 PUT /meme/<id> Изменение существующего мема        ПОЗ - НЕГ -
# 7 DELETE /meme/<id> Удаление мема                    ПОЗ - НЕГ -

# для позитивов добавить параметризацию
import pytest
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


# чистовик ПОЗ
# def test_get_memes(get_memes, check_token):
#     get_memes.get_all_memes(check_token)
#     get_memes.check_that_status_code_is_200()
#     get_memes.check_response_body_presence()
#     get_memes.check_response_structure()


# чистовик ПОЗ
# def test_get_meme_id(get_meme_id, check_token, create_test_meme_then_delete):
#     get_meme_id.get_meme_by_id(check_token, create_test_meme_then_delete)
#     get_meme_id.check_that_status_code_is_200()
#     get_meme_id.check_response_body_presence()
#     get_meme_id.check_response_structure()
#     get_meme_id.check_meme_id()


# чистовик ПОЗ
# def test_post_meme(post_meme, check_token):
#     body = {
#         "text": "description",
#         "url": "https://memes",
#         "tags": [
#             "first",
#             "second"
#         ],
#         "info": {
#             "additional info": "training mem"
#         }
#     }
#     post_meme.create_new_meme(check_token, body)
#     post_meme.check_that_status_code_is_200()
#     post_meme.check_response_body_presence()
#     post_meme.check_response_structure()
#
#     post_meme.delete_test_meme()


@pytest.mark.parametrize
def test_put_meme_id(put_meme_id, check_token, create_test_meme_then_delete):
    new_body = {
        "text": "new_description",
        "url": "https://memes/new/put",
        "tags": [
            "make a change",
            "put"
        ],
        "info": {
            "additional info": "training put"
        }
    }
    put_meme_id.put_meme_by_id(meme_id=create_test_meme_then_delete, token=check_token, body=new_body)
    put_meme_id.check_that_status_code_is_200()
    put_meme_id.check_response_body_presence()
    put_meme_id.check_response_structure()
    put_meme_id.check_meme_id()
    put_meme_id.check_updating_meme()