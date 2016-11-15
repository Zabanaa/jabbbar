from zabbbana.user import User
from . import jordan

TEST_USERNAME   = "kolage"
test_user       = User(jordan)

def test_get_user():
    response = test_user.get_details()
    assert 'username' in response

    response = test_user.get_details(username=TEST_USERNAME)
    assert response['username'] == TEST_USERNAME

def test_list_buckets():
    response = test_user.list_buckets()
    assert isinstance(response, list)

    response = test_user.list_buckets(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_projects():
    response = test_user.list_projects()
    assert isinstance(response, list)

    response = test_user.list_projects(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_shot_likes():
    response = test_user.list_shot_likes()
    assert isinstance(response, list)

    response = test_user.list_shot_likes(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_shots():
    response = test_user.list_shots()
    assert isinstance(response, list)

    response = test_user.list_shots(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_teams():
    response = test_user.list_teams()
    assert isinstance(response, list)

    response = test_user.list_teams(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_followers():
    response = test_user.list_followers()
    assert isinstance(response, list)

    response = test_user.list_followers(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_following():
    response = test_user.list_following()
    assert isinstance(response, list)

    response = test_user.list_following(username=TEST_USERNAME)
    assert isinstance(response, list)

def test_list_following_shots():
    response = test_user.list_shots_from_following()
    assert isinstance(response, list)

def test_check_user_is_following():

    # current user follows target user
    response = test_user.check_following(target_user=TEST_USERNAME)
    status_code = response.__dict__['status_code']
    assert status_code == 204

    # current user does not follow target user
    response = test_user.check_following("RypeArts")
    status_code = response.__dict__['status_code']
    assert status_code == 404

    # user does not follow target user
    response = test_user.check_following(username=TEST_USERNAME, target_user="MilkshakePanda")
    status_code = response.__dict__['status_code']
    assert status_code == 404

    # user follows the target user
    response = test_user.check_following(username=TEST_USERNAME, target_user="ghanipradita")
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_follow():
    response    = test_user.follow_user(target_user="luisamf")
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_unfollow():
    # follow ghani then unfollow him
    response    = test_user.follow_user(target_user="ghanipradita")
    status_code = response.__dict__['status_code']
    response    = test_user.unfollow_user(target_user="ghanipradita")
    assert status_code == 204

