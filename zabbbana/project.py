from zabbbana import Zabbbana as zbn
import requests as req

class Project(zbn):
    MAIN_ENDPOINT = "{}/projects".format(zbn.API_ENDPOINT)

    def __init__(self, inst, project_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.project_id = project_id

    def get_details(self, project_id=None):

        """ Get information about a specific project"""

        project_id      = project_id if project_id is not None else self.project_id
        endpoint        = "{}/{}".format(self.MAIN_ENDPOINT, project_id)
        project_details = req.get(endpoint, headers=self.auth_header)
        return project_details.json()

    def get_shots(self, project_id=None):

        """ Retrieves a list of all shots that are part of this project"""

        project_id      = project_id if project_id is not None else self.project_id
        endpoint        = "{}/{}/shots".format(self.MAIN_ENDPOINT, project_id)
        shots           = req.get(endpoint, headers=self.auth_header)
        return shots.json()
