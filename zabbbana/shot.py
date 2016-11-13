from zabbbana import Zabbbana as zbn
import requests as req

class Shot(zbn):

    MAIN_ENDPOINT = "{}/shots".format(zbn.API_ENDPOINT)

    def __init__(self, inst, shot_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.shot_id = shot_id

    # list_attachements
    # get_attachement
    # list_buckets
    # list_comments
    # list_likes
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

