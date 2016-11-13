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


    # get_comment
    # check_user_likes_comment
    # like_comment (write scope)
    # unlike_comment (write scope)
    # list_likes
    # check_user_likes_shot
    # like
    # unlike
    # list_projects
    # list_rebounds

