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

        """ Retrieve a list of all uploaded shots on the site"""

        shots = req.get(self.MAIN_ENDPOINT, headers=self.auth_header, params=params)
        return shots.json()

    def get_one(self, shot_id):

        """ Get details for a specific shot"""

        endpoint    = "{}/{}".format(self.MAIN_ENDPOINT, shot_id)
        shot_info   = req.get(endpoint, headers=self.auth_header)
        return shot_info.json()

    def upload(self, params):

        """ Uploads a shot to the user's account (the user must be authenticated with the upload scope,
        he/she also must be a drafted player"""

        upload_shot = req.post(self.MAIN_ENDPOINT, headers=self.auth_header, params=params)
        return upload_shot

    def update(self, shot_id, params):

        """ Update information about a shot"""

        pass

    def delete(self, shot_id):

        """ Delete a specific shot"""

        pass
