from zabbbana import Zabbbana as zbn
import requests as req

class Project(zbn):
    MAIN_ENDPOINT = "{}/projects".format(zbn.API_ENDPOINT)

    def __init__(self, inst):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)

    def get_details(self, project_id=None):
        project_details = req.get("{}/{}".format(self.MAIN_ENDPOINT, project_id), headers=self.auth_header)
        response        = project_details.json()
        return response
