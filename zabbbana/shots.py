from zabbbana import Zabbbana as zbn
import requests as req

class Shots(zbn):

    MAIN_ENDPOINT = "{}/shots".format(zbn.API_ENDPOINT)

    def __init__(self, inst):
        zbn.__init__(
            self,
            client_id=inst.client_id,
            client_secret=inst.client_secret,
            access_token=inst.access_token
        )

    def list_all(self, params):
        shots = req.get(self.MAIN_ENDPOINT, headers=self.auth_header, params=params)
        return shots.json()

    def get_one(self, shot_id):
        shot_info = req.get("{}/{}".format(self.MAIN_ENDPOINT, shot_id), headers=self.auth_header)
        return shot_info.json()

    def upload(self, params, shot_data, shot_content_type):
        shot_data   = {'image': ('image', shot_data, shot_content_type)}
        upload_shot = req.post(self.MAIN_ENDPOINT, headers=self.auth_header, params=params)
        return upload_shot()

