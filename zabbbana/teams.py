from zabbbana import Zabbbana as zbn
import requests as req

class Team(zbn):

    MAIN_ENDPOINT = "{}/teams".format(zbn.API_ENDPOINT)

    def __init__(self, inst, team_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.team_id = str(team_id)


    def list_players(self, team_id=None):
        team_id             = str(team_id) if team_id is not None else self.team_id
        endpoint            = "{}/{}/members".format(self.MAIN_ENDPOINT, team_id)
        team_players        = req.get(endpoint, headers=self.auth_header)
        return team_players.json()


    def list_shots(self, team_id=None):
        team_id             = str(team_id) if team_id is not None else self.team_id
        endpoint            = "{}/{}/shots".format(self.MAIN_ENDPOINT, team_id)
        team_shots          = req.get(endpoint, headers=self.auth_header)
        return team_shots.json()
