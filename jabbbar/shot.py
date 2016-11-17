class Shot():

    def __init__(self, client, shot_id=None):
        self.client  = client
        self.shot_id = shot_id

    def list_all(self, params):

        """
            Retrieve a list of all uploaded shots on the site
            http://developer.dribbble.com/v1/shots/#list-shots
        """

        shots = self.client.GET("/shots")
        return shots.json()

    def get_one(self, shot_id=None):

        """
            Get details for a specific shot
            http://developer.dribbble.com/v1/shots/#get-a-shot
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        shot_info   = self.client.GET("/shots/{}".format(shot_id))
        return shot_info.json()

    def list_attachments(self, shot_id=None):

        """
            List attachments for a shot
            http://developer.dribbble.com/v1/shots/attachments/#list-attachments-for-a-shot
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        attachments         = self.client.GET("/shots/{}/attachments".format(shot_id))
        return attachments.json()

    def get_attachment(self, attachment_id, shot_id=None):

        """
            get a single attachment for shot
            http://developer.dribbble.com/v1/shots/attachments/#get-a-single-attachment
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        attachment          = self.client.GET("/shots/{}/attachments/{}".format(shot_id, attachment_id))
        return attachment.json()

    def list_buckets(self, shot_id=None):

        """
            List all buckets a shot is part of
            http://developer.dribbble.com/v1/shots/buckets/
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        buckets             = self.client.GET("/shots/{}/buckets".format(shot_id))
        return buckets.json()

    def list_comments(self, shot_id=None):
        """
            List all the comments for a shot
            http://developer.dribbble.com/v1/shots/comments/#list-comments-for-a-shot
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        comments            = self.client.GET("/shots/{}/comments".format(shot_id))
        return comments.json()

    def list_comment_likes(self, comment_id, shot_id=None):

        """
            List all likes for a single comment in a single shot
            http://developer.dribbble.com/v1/shots/comments/#list-likes-for-a-comment
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        comment_likes           = self.client.GET("/shots/{}/comments/{}/likes".format(shot_id, comment_id))
        return comment_likes.json()

    def get_comment(self, comment_id, shot_id=None):

        """
            Get a single comment for a single shot
            http://developer.dribbble.com/v1/shots/comments/#get-a-single-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        comment                 = self.client.GET("/shots/{}/comments/{}".format(shot_id, comment_id))
        return comment.json()


    def like_comment(self, comment_id, shot_id=None):


        """
            Add like to a single comment
            http://developer.dribbble.com/v1/shots/comments/#like-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        like                    = self.client.POST("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return like.json()

    def unlike_comment(self, comment_id, shot_id=None):

        """
            Unlikes a previously liked comment
            http://developer.dribbble.com/v1/shots/comments/#unlike-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        unlike                  = self.client.DELETE("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return unlike

    def list_likes(self, shot_id=None):

        """
            List all the likes for a shot
            http://developer.dribbble.com/v1/shots/likes/#list-the-likes-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        shot_likes              = self.client.GET("/shots/{}/likes".format(shot_id))
        return shot_likes.json()

    def like(self, shot_id=None):

        """
            Like a single shot
            http://developer.dribbble.com/v1/shots/likes/#like-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        like                    = self.client.POST("/shots/{}/like".format(shot_id))
        return like.json()

    def unlike(self, shot_id=None):

        """
            Unlike a single shot
            http://developer.dribbble.com/v1/shots/likes/#unlike-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        unlike                  = self.client.DELETE("/shots/{}/like".format(shot_id))
        return unlike

    def list_projects(self, shot_id=None):

        """
            List all the projects for a shot
            http://developer.dribbble.com/v1/shots/projects/#list-projects-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        projects                = self.client.GET("/shots/{}/projects".format(shot_id))
        return projects.json()

    def list_rebounds(self, shot_id=None):

        """
            List all the rebounds for a shot
            http://developer.dribbble.com/v1/shots/rebounds/
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        projects                = self.client.GET("/shots/{}/rebounds".format(shot_id))
        return projects.json()
