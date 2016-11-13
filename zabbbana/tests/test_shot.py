from zabbbana.shot import Shot
from . import jordan

DEFAULT_SHOT_ID            = 1757843
DEFAULT_COMMENT_ID         = 3991565
EXTERNAL_SHOT_ID           = 3064133
EXTERNAL_COMMENT_ID        = 5690090
DEFAULT_ATTACHEMENT_ID     = 285772
test_shot = Shot(jordan, DEFAULT_SHOT_ID)

def test_list_attachments():
    # Without ID
    response            = test_shot.list_attachments()
    attachment_object  = response[0]
    assert 'thumbnail_url' in attachment_object

    # With ID
    response            = test_shot.list_attachments(shot_id=3085980)
    attachment_object  = response[0]
    assert 'thumbnail_url' in attachment_object

def test_get_attachment():
    # Without ID (Default ID)
    response            = test_shot.get_attachment(DEFAULT_ATTACHEMENT_ID)
    assert 'thumbnail_url' in response

    # With ID
    response            = test_shot.get_attachment(644444, shot_id=EXTERNAL_SHOT_ID)
    assert 'thumbnail_url' in response

def test_list_buckets():
    # Without ID (Default ID)
    response            = test_shot.list_buckets()
    first_bucket        = response[0]
    assert 'name' in first_bucket

    # With ID
    response            = test_shot.list_buckets(shot_id=EXTERNAL_SHOT_ID)
    first_bucket        = response[0]
    assert 'name' in first_bucket

def test_list_comments():
    # Without ID (Default ID)
    response            = test_shot.list_comments()
    first_comment       = response[0]
    assert 'body' in first_comment

    # With ID
    response            = test_shot.list_comments(shot_id=EXTERNAL_SHOT_ID)
    first_comment       = response[0]
    assert 'body' in first_comment

def test_comment_likes():
    # Without ID (Default ID)
    response            = test_shot.list_comment_likes(DEFAULT_COMMENT_ID)
    first_comment_like  = response[0]
    assert 'id' in first_comment_like

    # With ID
    response            = test_shot.list_comment_likes(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    first_comment_like  = response[0]
    assert 'id' in first_comment_like

def test_get_comment():
    # Without ID (Default ID)
    response            = test_shot.get_comment(DEFAULT_COMMENT_ID)
    assert 'created_at' in response

    # With ID
    response            = test_shot.get_comment(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

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
