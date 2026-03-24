import pytest

user = {"name": "Wowa"}
name = user['name']

# тестовые данные для обновления мемов
create_bodies_positive = [
    {"text": "1 description", "url": "https://memes/one", "tags": ["first", "second"],
     "info": {"additional info": "training mem"}},

    {"text": "2 description", "url": "https://memes/two", "tags": ["second"],
     "info": {"additional info": "training mem"}},

    {"text": "3 description", "url": "https://memes/three", "tags": ["third"],
     "info": {"additional info": "training mem"}},

    {"text": "4 description", "url": "https://memes/four", "tags": ["forth"],
     "info": {"additional info": "training mem"}}
]
put_bodies_positive = [
    {"text": "2_description", "url": "https://memes/new/put", "tags": ["make a change", "put"],
     "info": {"additional info": "training 2 put"}},

    {"text": "3_description", "url": "https://memes/new/put", "tags": ["make a change", "put"],
     "info": {"additional info": "training 3 put"}},

    {"text": "4_description", "url": "https://memes/new/put", "tags": ["make a change", "put"],
     "info": {"additional info": "training 4 put"}},

    {"text": "5_description", "url": "https://memes/new/put", "tags": ["make a change", "put"],
     "info": {"additional info": "training 5 put"}},
]


def test_post_authorize(check_token, post_authorize):
    post_authorize.generate_new_token(user)
    post_authorize.check_that_status_code_is_200()
    post_authorize.check_response_body_presence()
    post_authorize.check_response_structure()


def test_get_authorize_token(get_authorize_token, check_token):
    get_authorize_token.checking_auth_token(check_token, name)
    get_authorize_token.check_that_status_code_is_200()

 # Одна проверка падает (id не int)
def test_get_memes(get_memes, check_token):
    get_memes.get_all_memes(check_token)
    get_memes.check_that_status_code_is_200()
    get_memes.check_response_body_presence()
    get_memes.check_response_structure()


def test_get_meme_id(get_meme_id, check_token, create_test_meme_then_delete):
    get_meme_id.get_meme_by_id(check_token, create_test_meme_then_delete)
    get_meme_id.check_that_status_code_is_200()
    get_meme_id.check_response_body_presence()
    get_meme_id.check_response_structure()
    get_meme_id.check_meme_id()


@pytest.mark.parametrize("body", create_bodies_positive)
def test_post_meme(post_meme, check_token, body):
    post_meme.create_new_meme(token=check_token, body=body)
    post_meme.check_that_status_code_is_200()
    post_meme.check_response_body_presence()
    post_meme.check_response_structure()
    post_meme.check_response_data(body)

    post_meme.delete_test_meme()


@pytest.mark.parametrize("new_body", put_bodies_positive)
def test_put_meme_id(put_meme_id, check_token, create_test_meme_then_delete, new_body):
    put_meme_id.put_meme_by_id(meme_id=create_test_meme_then_delete, token=check_token, body=new_body)
    put_meme_id.check_that_status_code_is_200()
    put_meme_id.check_response_body_presence()
    put_meme_id.check_response_structure()
    put_meme_id.check_meme_id()
    put_meme_id.check_response_data(new_body)


def test_delete_meme_id(delete_meme_id, check_token):
    delete_meme_id.create_test_meme(token=check_token)
    delete_meme_id.delete_meme()
    delete_meme_id.check_that_meme_has_been_deleted()
