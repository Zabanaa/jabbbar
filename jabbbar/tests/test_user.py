import time
from jabbbar import User
from . import client, userless_client

DEFAULT_SHOT_ID            = 1757843
DEFAULT_COMMENT_ID         = 3991565
EXTERNAL_SHOT_ID           = 3064133
EXTERNAL_COMMENT_ID        = 5690090
DEFAULT_ATTACHEMENT_ID     = 285772
TEST_USERNAME           = "kolage"
test_user               = User(client)
userless_requester      = User(client)

class TestUser():
    def test_get_user(self):
        # Get details for the authenticated user
        time.sleep(2)
        response = test_user.get_details()
        assert 'username' in response

        # Get details for a specific user
        time.sleep(2)
        response = test_user.get_details(username=TEST_USERNAME)
        assert response['username'] == TEST_USERNAME

    def test_list_buckets(self):
        # List buckets for the current user
        response = test_user.list_buckets()
        time.sleep(2)
        assert isinstance(response, list)

        # List buckets for the another user
        time.sleep(2)
        response = test_user.list_buckets(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_projects(self):
        # List projects for the current user
        time.sleep(2)
        response = test_user.list_projects()
        assert isinstance(response, list)

        # List projects for the another user
        time.sleep(2)
        response = test_user.list_projects(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_shot_likes(self):
        # List shot likes for the current user
        time.sleep(2)
        response = test_user.list_shot_likes()
        assert isinstance(response, list)

        # List shot likes for the another user
        time.sleep(2)
        response = test_user.list_shot_likes(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_shots(self):
        # List shot for the current user
        time.sleep(2)
        response = test_user.list_shots()
        assert isinstance(response, list)

        # List shot for the another user
        time.sleep(2)
        response = test_user.list_shots(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_teams(self):
        # List teams for the current user
        time.sleep(2)
        response = test_user.list_teams()
        assert isinstance(response, list)

        # List teams for the another user
        time.sleep(2)
        response = test_user.list_teams(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_followers(self):
        # List followers for the current user
        time.sleep(2)
        response = test_user.list_followers()
        assert isinstance(response, list)

        # List followers for the another user
        time.sleep(2)
        response = test_user.list_followers(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_following(self):
        # List following users for the current user
        time.sleep(2)
        response = test_user.list_following()
        assert isinstance(response, list)

        # List following users for the another user
        time.sleep(2)
        response = test_user.list_following(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_following_shots(self):
        time.sleep(2)
        response = test_user.list_shots_from_following()
        assert isinstance(response, list)

    def test_check_user_is_following(self):

        time.sleep(2)
        # current user follows target user
        response = test_user.check_following(target_user=TEST_USERNAME)
        status_code = response.__dict__['status_code']
        assert status_code == 204

        time.sleep(2)
        # current user does not follow target user
        response = test_user.check_following("RypeArts")
        status_code = response.__dict__['status_code']
        assert status_code == 404

        time.sleep(2)
        # user does not follow target user
        response = test_user.check_following(username=TEST_USERNAME, target_user="MilkshakePanda")
        status_code = response.__dict__['status_code']
        assert status_code == 404

        time.sleep(2)
        # user follows the target user
        response = test_user.check_following(username=TEST_USERNAME, target_user="ghanipradita")
        status_code = response.__dict__['status_code']
        assert status_code == 204

    def test_follow(self):
        time.sleep(2)
        response    = test_user.follow_user(target_user="luisamf")
        status_code = response.__dict__['status_code']
        assert status_code == 204

    def test_unfollow(self):
        # follow ghani then unfollow him
        time.sleep(2)
        response    = test_user.follow_user(target_user="ghanipradita")
        status_code = response.__dict__['status_code']
        response    = test_user.unfollow_user(target_user="ghanipradita")
        assert status_code == 204

    def test_check_user_likes_shot(self):
        # If the current user likes the shot it should return 200 along with an object
        time.sleep(2)
        response            = test_user.check_user_likes_shot(DEFAULT_SHOT_ID)
        status_code         = response.__dict__['status_code']
        assert status_code == 200

        # If the current user does not like
        time.sleep(2)
        response            = test_user.check_user_likes_shot(EXTERNAL_SHOT_ID)
        status_code         = response.__dict__['status_code']
        assert status_code == 404

    def test_check_user_likes_comment(self):
        # User Does Not Like The Comment
        time.sleep(2)
        response            = test_user.check_user_likes_comment(DEFAULT_COMMENT_ID, DEFAULT_SHOT_ID)
        status_code         = response.__dict__['status_code']
        assert status_code == 404

        # User likes the comment
        time.sleep(2)
        response            = test_user.check_user_likes_comment(DEFAULT_COMMENT_ID + 2, DEFAULT_SHOT_ID)
        status_code         = response.__dict__['status_code']
        assert status_code == 200

    def test_upload_shot(self):
        pass

    def test_update_shot(self):
        pass

    def test_delete_shot(self):
        pass

class TestUserlessUser():
    def test_get_user(self):
        time.sleep(2)
        response = userless_requester.get_details(username=TEST_USERNAME)
        assert response['username'] == TEST_USERNAME

    def test_list_buckets(self):
        time.sleep(2)
        response = userless_requester.list_buckets(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_projects(self):
        time.sleep(2)
        response = userless_requester.list_projects(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_shot_likes(self):
        time.sleep(2)
        response = userless_requester.list_shot_likes(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_shots(self):
        time.sleep(2)
        response = userless_requester.list_shots(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_teams(self):
        time.sleep(2)
        response = userless_requester.list_teams(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_followers(self):
        time.sleep(2)
        response = userless_requester.list_followers(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_following(self):
        time.sleep(2)
        response = userless_requester.list_following(username=TEST_USERNAME)
        assert isinstance(response, list)

    def test_list_following_shots(self):
        time.sleep(2)
        response = userless_requester.list_shots_from_following()
        assert isinstance(response, list)
