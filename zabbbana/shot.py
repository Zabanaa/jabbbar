from zabbbana import Zabbbana as zbn
import requests as req

class Shot(zbn):

    MAIN_ENDPOINT = "{}/shots".format(zbn.API_ENDPOINT)

    def __init__(self, inst, shot_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.shot_id = shot_id



