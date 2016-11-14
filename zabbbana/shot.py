from zabbbana import Zabbbana as zbn
import requests as req

class Shot(zbn):

    MAIN_ENDPOINT = "{}/shots".format(zbn.API_ENDPOINT)

    def __init__(self, inst, shot_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.shot_id = shot_id

    def list_attachments(self, shot_id=None):

        """
            List attachments for a shot
            http://developer.dribbble.com/v1/shots/attachments/#list-attachments-for-a-shot
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/attachments".format(self.MAIN_ENDPOINT, shot_id)
        attachments         = req.get(endpoint, headers=self.auth_header)
        return attachments.json()

    def get_attachment(self, attachment_id, shot_id=None):

        """
            get a single attachment for shot
            http://developer.dribbble.com/v1/shots/attachments/#get-a-single-attachment
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/attachments/{}".format(self.MAIN_ENDPOINT, shot_id, attachment_id)
        attachment          = req.get(endpoint, headers=self.auth_header)
        return attachment.json()

    def list_buckets(self, shot_id=None):

        """
            List all buckets a shot is part of
            http://developer.dribbble.com/v1/shots/buckets/
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/buckets".format(self.MAIN_ENDPOINT, shot_id)
        buckets             = req.get(endpoint, headers=self.auth_header)
        return buckets.json()

    def list_comments(self, shot_id=None):
        """
            List all the comments for a shot
            http://developer.dribbble.com/v1/shots/comments/#list-comments-for-a-shot
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/comments".format(self.MAIN_ENDPOINT, shot_id)
        comments            = req.get(endpoint, headers=self.auth_header)
        return comments.json()

    def list_comment_likes(self, comment_id, shot_id=None):

        """
            List all likes for a single comment in a single shot
            http://developer.dribbble.com/v1/shots/comments/#list-likes-for-a-comment
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/likes".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        comment_likes           = req.get(endpoint, headers=self.auth_header)
        return comment_likes.json()

    def get_comment(self, comment_id, shot_id=None):

        """
            Get a single comment for a single shot
            http://developer.dribbble.com/v1/shots/comments/#get-a-single-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        comment                 = req.get(endpoint, headers=self.auth_header)
        return comment.json()

    def check_user_likes_comment(self, comment_id, shot_id=None):

        """
            Check if the authenticated user likes a comment
            http://developer.dribbble.com/v1/shots/comments/#check-if-you-like-a-comment
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        result                  = req.get(endpoint, headers=self.auth_header)
        return result

    def like_comment(self, comment_id, shot_id=None):


        """
            Add like to a single comment
            http://developer.dribbble.com/v1/shots/comments/#like-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        like                    = req.post(endpoint, headers=self.auth_header)
        return like.json()

    def unlike_comment(self, comment_id, shot_id=None):

        """
            Unlikes a previously liked comment
            http://developer.dribbble.com/v1/shots/comments/#unlike-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        unlike                    = req.delete(endpoint, headers=self.auth_header)
        return unlike

    def list_likes(self, shot_id=None):

        """
            List all the likes for a shot
            http://developer.dribbble.com/v1/shots/likes/#list-the-likes-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/likes".format(self.MAIN_ENDPOINT, shot_id)
        shot_likes              = req.get(endpoint, headers=self.auth_header)
        return shot_likes.json()

    def like(self, shot_id=None):

        """
            Like a single shot
            http://developer.dribbble.com/v1/shots/likes/#like-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/like".format(self.MAIN_ENDPOINT, shot_id)
        like                    = req.post(endpoint, headers=self.auth_header)
        return like.json()

    def unlike(self, shot_id=None):

        """
            Unlike a single shot
            http://developer.dribbble.com/v1/shots/likes/#unlike-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/like".format(self.MAIN_ENDPOINT, shot_id)
        unlike                  = req.delete(endpoint, headers=self.auth_header)
        return unlike

    def list_projects(self, shot_id=None):

        """
            List all the projects for a shot
            http://developer.dribbble.com/v1/shots/projects/#list-projects-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/projects".format(self.MAIN_ENDPOINT, shot_id)
        projects                = req.get(endpoint, headers=self.auth_header)
        return projects.json()

    def list_rebounds(self, shot_id=None):

        """
            List all the rebounds for a shot
            http://developer.dribbble.com/v1/shots/rebounds/
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/rebounds".format(self.MAIN_ENDPOINT, shot_id)
        projects                = req.get(endpoint, headers=self.auth_header)
        return projects.json()

    def check_user_likes_shot(self, shot_id=None):

        """
            Checks if the authenticated user likes a single shot
            http://developer.dribbble.com/v1/shots/likes/#check-if-you-like-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/like".format(self.MAIN_ENDPOINT, shot_id)
        like_shot               = req.get(endpoint, headers=self.auth_header)
        return like_shot
