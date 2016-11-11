from zabbbana import Zabbbana as zbn
import requests as req

class Project(zbn):
    MAIN_ENDPOINT = "{}/projects".format(zbn.API_ENDPOINT)

    def __init__(self, inst, project_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.project_id = project_id

    def get_details(self, project_id=None):

        if project_id:
            project_id = project_id
        else:
            project_id = self.project_id

        project_details = req.get("{}/{}".format(self.MAIN_ENDPOINT, project_id), headers=self.auth_header)
        response        = project_details.json()
        return response

    def get_shots(self, project_id=None):

        if project_id:
            project_id = project_id
        else:
            project_id = self.project_id

        shots    = req.get("{}/{}/shots".format(self.MAIN_ENDPOINT, project_id), headers=self.auth_header)
        response = shots.json()
        return response
