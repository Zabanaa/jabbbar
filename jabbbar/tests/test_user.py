import time
from jabbbar import User
from . import client

DEFAULT_SHOT_ID            = 1757843
DEFAULT_COMMENT_ID         = 3991565
EXTERNAL_SHOT_ID           = 3064133
EXTERNAL_COMMENT_ID        = 5690090
DEFAULT_ATTACHEMENT_ID     = 285772
TEST_USERNAME   = "kolage"
test_user       = User(client)

def test_get_user():
    time.sleep(1.1)
    response = test_user.get_details()
    assert 'username' in response

    time.sleep(1.1)
    response = test_user.get_details(username=TEST_USERNAME)
    assert response['username'] == TEST_USERNAME

def test_list_buckets():
    response = test_user.list_buckets()
    time.sleep(1.1)
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_buckets(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_projects():
    time.sleep(1.1)
    response = test_user.list_projects()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_projects(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_shot_likes():
    time.sleep(1.1)
    response = test_user.list_shot_likes()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_shot_likes(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_shots():
    time.sleep(1.1)
    response = test_user.list_shots()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_shots(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_teams():
    time.sleep(1.1)
    response = test_user.list_teams()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_teams(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_followers():
    time.sleep(1.1)
    response = test_user.list_followers()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_followers(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_following():
    time.sleep(1.1)
    response = test_user.list_following()
    assert isinstance(response, list)

    time.sleep(1.1)
    response = test_user.list_following(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_following_shots():
    time.sleep(1.1)
    response = test_user.list_shots_from_following()
    assert isinstance(response, list)

def test_check_user_is_following():

    time.sleep(1.1)
    # current user follows target user
    response = test_user.check_following(target_user=TEST_USERNAME)
    status_code = response.__dict__['status_code']
    assert status_code == 204

    time.sleep(1.1)
    # current user does not follow target user
    response = test_user.check_following("RypeArts")
    status_code = response.__dict__['status_code']
    assert status_code == 404

    time.sleep(1.1)
    # user does not follow target user
    response = test_user.check_following(username=TEST_USERNAME, target_user="MilkshakePanda")
    status_code = response.__dict__['status_code']
    assert status_code == 404

    time.sleep(1.1)
    # user follows the target user
    response = test_user.check_following(username=TEST_USERNAME, target_user="ghanipradita")
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_follow():
    time.sleep(1.1)
    response    = test_user.follow_user(target_user="luisamf")
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_unfollow():
    # follow ghani then unfollow him
    time.sleep(1.1)
    response    = test_user.follow_user(target_user="ghanipradita")
    status_code = response.__dict__['status_code']
    response    = test_user.unfollow_user(target_user="ghanipradita")
    assert status_code == 204

def test_upload_shot():
    pass

def test_update_shot():
    pass

def test_delete_shot():
    pass

def test_check_user_likes_shot():
    # If the current user likes the shot it should return 200 along with an object
    time.sleep(1.1)
    response            = test_user.check_user_likes_shot(DEFAULT_SHOT_ID)
    status_code         = response.__dict__['status_code']
    assert status_code == 200

    # If the current user does not like
    time.sleep(1.1)
    response            = test_user.check_user_likes_shot(EXTERNAL_SHOT_ID)
    status_code         = response.__dict__['status_code']
    assert status_code == 404

def test_check_user_likes_comment():
    # User Does Not Like The Comment
    time.sleep(1.1)
    response            = test_user.check_user_likes_comment(DEFAULT_COMMENT_ID, DEFAULT_SHOT_ID)
    status_code         = response.__dict__['status_code']
    assert status_code == 404

    # User likes the comment
    time.sleep(1.1)
    response            = test_user.check_user_likes_comment(DEFAULT_COMMENT_ID + 2, DEFAULT_SHOT_ID)
    status_code         = response.__dict__['status_code']
    assert status_code == 200
