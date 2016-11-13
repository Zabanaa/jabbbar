from zabbbana.shot import Shot
from . import jordan

DEFAULT_SHOT_ID = 1757843
DEFAULT_ATTACHEMENT_ID = 285772
test_shot = Shot(jordan, DEFAULT_SHOT_ID)

def test_list_attachements():
    response            = test_shot.list_attachements()
    attachement_object  = response[0]
    assert 'thumbnail_url' in attachement_object

def test_get_attachement():
    response            = test_shot.get_attachement(DEFAULT_ATTACHEMENT_ID)
    assert 'thumbnail_url' in response

def test_list_buckets():
    pass

def test_list_comments():
    pass

def test_list_likes():
    pass

def test_get_comment():
    pass

def test_check_user_likes_comment():
    pass

def test_like_comment():
    pass

def test_unlike_comment():
    pass

def test_list_likes():
    pass

def test_check_user_likes_shot():
    pass

def test_like_shot():
    pass

def test_unlike_shot():
    pass

def test_list_projects():
    pass

def test_list_rebounds():
    pass
