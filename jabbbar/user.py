class User():

    def __init__(self, client):
        self.client     = client

    def get_details(self, username=None):

        if username is not None:
            user_details        = self.client.GET("/users/{username}".format(username=username))
        else:
            user_details        = self.client.GET("/user")

        return user_details.json()

    def list_buckets(self, username=None):

        if username is not None:
            buckets             = self.client.GET("/users/{username}/buckets".format(username=username))
        else:
            buckets             = self.client.GET("/user/buckets")

        return buckets.json()

    def list_shot_likes(self, username=None):

        if username is not None:
            shot_likes          = self.client.GET("/users/{username}/likes".format(username=username))
        else:
            shot_likes          = self.client.GET("/user/likes")

        return shot_likes.json()

    def list_projects(self, username=None):

        if username is not None:
            projects            = self.client.GET("/users/{username}/projects".format(username=username))
        else:
            projects            = self.client.GET("/user/projects")

        return projects.json()

    def list_shots(self, username=None):

        if username is not None:
            shots               = self.client.GET("/users/{username}/shots".format(username=username))
        else:
            shots               = self.client.GET("/user/shots")

        return shots.json()

    def list_teams(self, username=None):

        if username is not None:
            teams               = self.client.GET("/users/{username}/teams".format(username=username))
        else:
            teams               = self.client.GET("/user/teams")

        return teams.json()

    def list_followers(self, username=None):

        if username is not None:
            followers               = self.client.GET("/users/{username}/followers".format(username=username))
        else:
            followers               = self.client.GET("/user/followers")

        return followers.json()

    def list_following(self, username=None):

        if username is not None:
            following               = self.client.GET("/users/{username}/following".format(username=username))
        else:
            following               = self.client.GET("/user/following")

        return following.json()

    def list_shots_from_following(self):

        shots_from_following        = self.client.GET("/user/following/shots")
        return shots_from_following.json()

    def check_following(self, username=None, target_user=None):
        if username is not None:
            following_user          = self.client.GET("/users/{username}/following/{target_user}".format(username=username,
                                                                                             target_user=target_user))
        else:
            following_user          = self.client.GET("/user/following/{target_user}".format(target_user=target_user))

        return following_user

    # follow
    def follow_user(self, target_user):
        follow_user_response        = self.client.PUT("/users/{target_user}/follow".format(target_user=target_user))
        return follow_user_response

    # unfollow
    def unfollow_user(self, target_user):
        unfollow_user_response      = self.client.DELETE("/users/{target_user}/follow".format(target_user=target_user))
        return unfollow_user_response

    def upload_shot(self, shot_data):

        """
            Uploads a shot to the user's account (the user must be authenticated with the upload scope,
        he/she also must be a drafted player
            http://developer.dribbble.com/v1/shots/#create-a-shot
        """
        pass

    def update_shot(self, shot_id, shot_data):

        """
            Update information about a shot
            http://developer.dribbble.com/v1/shots/#update-a-shot
        """
        pass

    def delete_shot(self, shot_id):

        """
            Delete a specific shot
            http://developer.dribbble.com/v1/shots/#delete-a-shot
        """
        pass

    def check_user_likes_shot(self, shot_id):

        """
            Checks if the authenticated user likes a single shot
            http://developer.dribbble.com/v1/shots/likes/#check-if-you-like-a-shot
        """
        like_shot               = self.client.GET("/shots/{}/like".format(shot_id))
        return like_shot

    def check_user_likes_comment(self, comment_id, shot_id):
        """
            Check if the authenticated user likes a comment
            http://developer.dribbble.com/v1/shots/comments/#check-if-you-like-a-comment
        """

        result                  = self.client.GET("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return result
