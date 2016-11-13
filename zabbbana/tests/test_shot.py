from zabbbana.shot import Shot
from . import jordan

DEFAULT_SHOT_ID            = 1757843
DEFAULT_COMMENT_ID         = 3991565
EXTERNAL_SHOT_ID           = 3064133
EXTERNAL_COMMENT_ID        = 5690090
DEFAULT_ATTACHEMENT_ID     = 285772
test_shot = Shot(jordan, DEFAULT_SHOT_ID)

def test_list_attachments():
    # List attachements for the instanciated shot
    response            = test_shot.list_attachments()
    attachment_object  = response[0]
    assert 'thumbnail_url' in attachment_object

    # List attachements for an external shot
    response            = test_shot.list_attachments(shot_id=3085980)
    attachment_object  = response[0]
    assert 'thumbnail_url' in attachment_object

def test_get_attachment():
    # Get attachement for the instanciated shot
    response            = test_shot.get_attachment(DEFAULT_ATTACHEMENT_ID)
    assert 'thumbnail_url' in response

    # Get attachement for an external shot
    response            = test_shot.get_attachment(644444, shot_id=EXTERNAL_SHOT_ID)
    assert 'thumbnail_url' in response

def test_list_buckets():
    # List buckets for the instance shot
    response            = test_shot.list_buckets()
    first_bucket        = response[0]
    assert 'name' in first_bucket

    # List buckets for an external shot
    response            = test_shot.list_buckets(shot_id=EXTERNAL_SHOT_ID)
    first_bucket        = response[0]
    assert 'name' in first_bucket

def test_list_comments():
    # List all the comments for the instanciated shot
    response            = test_shot.list_comments()
    first_comment       = response[0]
    assert 'body' in first_comment

    # List all the comments for an external shot
    response            = test_shot.list_comments(shot_id=EXTERNAL_SHOT_ID)
    first_comment       = response[0]
    assert 'body' in first_comment

def test_comment_likes():
    # List comment likes for a comment in the instance shot
    response            = test_shot.list_comment_likes(DEFAULT_COMMENT_ID)
    first_comment_like  = response[0]
    assert 'id' in first_comment_like

    # List comment likes for a comment in an external shot
    response            = test_shot.list_comment_likes(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    first_comment_like  = response[0]
    assert 'id' in first_comment_like

def test_get_comment():
    # Get a comment from within the instance shot
    response            = test_shot.get_comment(DEFAULT_COMMENT_ID)
    assert 'created_at' in response

    # Get a comment from an external shot
    response            = test_shot.get_comment(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

def test_check_user_likes_comment():
    # User Does Not Like The Comment
    response            = test_shot.check_user_likes_comment(DEFAULT_COMMENT_ID)
    status_code         = response.__dict__['status_code']
    assert status_code == 404

    # User likes the comment
    response            = test_shot.check_user_likes_comment(DEFAULT_COMMENT_ID + 2)
    status_code         = response.__dict__['status_code']
    assert status_code == 200

def test_like_comment():
    # Like a comment in the instance's own shot
    response            = test_shot.like_comment(3991574)
    assert 'created_at' in response

    # Like a comment in an external shot
    response            = test_shot.like_comment(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

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
