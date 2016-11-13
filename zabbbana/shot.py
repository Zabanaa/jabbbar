from zabbbana import Zabbbana as zbn
import requests as req

class Shot(zbn):

    MAIN_ENDPOINT = "{}/shots".format(zbn.API_ENDPOINT)

    def __init__(self, inst, shot_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.shot_id = shot_id

    def list_attachments(self, shot_id=None):

        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/attachments".format(self.MAIN_ENDPOINT, shot_id)
        attachments         = req.get(endpoint, headers=self.auth_header)
        return attachments.json()

    def get_attachment(self, attachment_id, shot_id=None):

        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/attachments/{}".format(self.MAIN_ENDPOINT, shot_id, attachment_id)
        attachment          = req.get(endpoint, headers=self.auth_header)
        return attachment.json()

    def list_buckets(self, shot_id=None):
        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/buckets".format(self.MAIN_ENDPOINT, shot_id)
        buckets             = req.get(endpoint, headers=self.auth_header)
        return buckets.json()

    def list_comments(self, shot_id=None):
        shot_id             = shot_id if shot_id is not None else self.shot_id
        endpoint            = "{}/{}/comments".format(self.MAIN_ENDPOINT, shot_id)
        comments            = req.get(endpoint, headers=self.auth_header)
        return comments.json()

    def list_comment_likes(self, comment_id, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/likes".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        comment_likes           = req.get(endpoint, headers=self.auth_header)
        return comment_likes.json()

    def get_comment(self, comment_id, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        comment                 = req.get(endpoint, headers=self.auth_header)
        return comment.json()

    def check_user_likes_comment(self, comment_id, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        result                  = req.get(endpoint, headers=self.auth_header)
        return result

    def like_comment(self, comment_id, shot_id=None):
        """ requires write scope """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        like                    = req.post(endpoint, headers=self.auth_header)
        return like.json()

    def unlike_comment(self, comment_id, shot_id=None):
        """ requires write scope """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/comments/{}/like".format(self.MAIN_ENDPOINT, shot_id, comment_id)
        unlike                    = req.delete(endpoint, headers=self.auth_header)
        return unlike

    def list_likes(self, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/likes".format(self.MAIN_ENDPOINT, shot_id)
        shot_likes              = req.get(endpoint, headers=self.auth_header)
        return shot_likes.json()

    def like(self, shot_id=None):
        """ requires write scope """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/like".format(self.MAIN_ENDPOINT, shot_id)
        like                    = req.post(endpoint, headers=self.auth_header)
        return like.json()

    def unlike(self, shot_id=None):
        """ requires write scope """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/like".format(self.MAIN_ENDPOINT, shot_id)
        unlike                  = req.delete(endpoint, headers=self.auth_header)
        return unlike

    def list_projects(self, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/projects".format(self.MAIN_ENDPOINT, shot_id)
        projects                = req.get(endpoint, headers=self.auth_header)
        return projects.json()

    def list_rebounds(self, shot_id=None):
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        endpoint                = "{}/{}/rebounds".format(self.MAIN_ENDPOINT, shot_id)
        projects                = req.get(endpoint, headers=self.auth_header)
        return projects.json()
