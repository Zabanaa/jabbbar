import os
import time
from jabbbar import Shot
from . import client

DEFAULT_SHOT_ID            = 1757843
DEFAULT_COMMENT_ID         = 3991565
EXTERNAL_SHOT_ID           = 3064133
EXTERNAL_COMMENT_ID        = 5690090
DEFAULT_ATTACHEMENT_ID     = 285772
test_shot = Shot(client, shot_id=DEFAULT_SHOT_ID)

DEFAULT_SHOT_ID      = 471756

PATH_TO_IMG          = os.path.dirname(__file__)

DEFAULT_UPLOAD_PARAMS = {
    'title': 'Bruv new shot',
    'image': os.path.join(PATH_TO_IMG, 'sample.png'),
    'description': 'Testing shot uploading on this ting',
    'tags': ['mad ting'],
    'team_id': None,
    'rebound_source_id': None
}

DEFAULT_QUERY_PARAMS = {
    'list': 'debuts',
    'timeframe': 'month',
    'date': '20151121',
    'sort': 'comments'
}

def test_list_all():
    time.sleep(1.1)
    response = test_shot.list_all(DEFAULT_QUERY_PARAMS)
    assert isinstance(response, list)

def test_get_one():
    time.sleep(1.1)
    response = test_shot.get_one(DEFAULT_SHOT_ID)
    assert response['id'] == DEFAULT_SHOT_ID

    time.sleep(1.1)
    response = test_shot.get_one(1209392210321321)
    assert 'Not found.' in response['message']

def test_list_attachments():
    # List attachements for the instanciated shot
    time.sleep(1.1)
    response            = test_shot.list_attachments()
    attachment_object  = response[0]
    assert isinstance(response, list)
    assert 'thumbnail_url' in attachment_object

    # List attachements for an external shot
    time.sleep(1.1)
    response            = test_shot.list_attachments(shot_id=3085980)
    attachment_object  = response[0]
    assert isinstance(response, list)
    assert 'thumbnail_url' in attachment_object

def test_get_attachment():
    # Get attachement for the instanciated shot
    time.sleep(1.1)
    response            = test_shot.get_attachment(DEFAULT_ATTACHEMENT_ID)
    assert 'thumbnail_url' in response

    # Get attachement for an external shot
    time.sleep(1.1)
    response            = test_shot.get_attachment(644444, shot_id=EXTERNAL_SHOT_ID)
    assert 'thumbnail_url' in response

def test_list_buckets():
    # List buckets for the instance shot
    time.sleep(1.1)
    response            = test_shot.list_buckets()
    first_bucket        = response[0]
    assert isinstance(response, list)
    assert 'name' in first_bucket

    # List buckets for an external shot
    time.sleep(1.1)
    response            = test_shot.list_buckets(shot_id=EXTERNAL_SHOT_ID)
    first_bucket        = response[0]
    assert isinstance(response, list)
    assert 'name' in first_bucket

def test_list_comments():
    # List all the comments for the instanciated shot
    time.sleep(1.1)
    response            = test_shot.list_comments()
    first_comment       = response[0]
    assert isinstance(response, list)
    assert 'body' in first_comment

    # List all the comments for an external shot
    time.sleep(1.1)
    response            = test_shot.list_comments(shot_id=EXTERNAL_SHOT_ID)
    first_comment       = response[0]
    assert isinstance(response, list)
    assert 'body' in first_comment

def test_comment_likes():
    # List comment likes for a comment in the instance shot
    time.sleep(1.1)
    response            = test_shot.list_comment_likes(DEFAULT_COMMENT_ID)
    first_comment_like  = response[0]
    assert isinstance(response, list)
    assert 'id' in first_comment_like

    # List comment likes for a comment in an external shot
    time.sleep(1.1)
    response            = test_shot.list_comment_likes(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    first_comment_like  = response[0]
    assert isinstance(response, list)
    assert 'id' in first_comment_like

def test_get_comment():
    # Get a comment from within the instance shot
    time.sleep(1.1)
    response            = test_shot.get_comment(DEFAULT_COMMENT_ID)
    assert 'created_at' in response

    # Get a comment from an external shot
    time.sleep(1.1)
    response            = test_shot.get_comment(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

def test_like_comment():
    # Like a comment in the instance's own shot
    time.sleep(1.1)
    response            = test_shot.like_comment(3991574)
    assert 'created_at' in response

    # Like a comment in an external shot
    time.sleep(1.1)
    response            = test_shot.like_comment(EXTERNAL_COMMENT_ID, shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

def test_unlike_comment():
    time.sleep(1.1)
    like                = test_shot.like_comment(3991757)
    unlike              = test_shot.unlike_comment(3991757)
    status_code         = unlike.__dict__['status_code']
    assert status_code == 204

def test_list_likes():
    # List all the likes for the instanciated shot
    time.sleep(1.1)
    response            = test_shot.list_likes()
    first_like          = response[0]
    assert isinstance(response, list)
    assert 'id' in first_like

    # List all the likes for an external shot
    time.sleep(1.1)
    response            = test_shot.list_likes(shot_id=EXTERNAL_SHOT_ID)
    first_like          = response[0]
    assert isinstance(response, list)
    assert 'id' in first_like

def test_check_user_likes_shot():
    pass

def test_like_shot():
    # Add like to the instanciated shot
    time.sleep(1.1)
    response            = test_shot.like()
    assert 'created_at' in response

    # Add like to an external shot
    time.sleep(1.1)
    response            = test_shot.like(shot_id=EXTERNAL_SHOT_ID)
    assert 'created_at' in response

def test_unlike_shot():
    time.sleep(1.1)
    like                = test_shot.like(shot_id=EXTERNAL_SHOT_ID)
    unlike              = test_shot.unlike(shot_id=EXTERNAL_SHOT_ID)
    status_code         = unlike.__dict__['status_code']
    assert status_code == 204

def test_list_projects():
    # List projects for the instanciated Shot
    time.sleep(1.1)
    response            = test_shot.list_projects()
    assert isinstance(response, list)

    # List projects for an external shot
    time.sleep(1.1)
    response            = test_shot.list_projects(shot_id=EXTERNAL_SHOT_ID)
    assert isinstance(response, list)

def test_list_rebounds():
    # List rebounds for the instanciated Shot
    time.sleep(1.1)
    response            = test_shot.list_rebounds()
    assert isinstance(response, list)

    # List rebounds for an external shot
    time.sleep(1.1)
    response            = test_shot.list_rebounds(shot_id=EXTERNAL_SHOT_ID)
    assert isinstance(response, list)

