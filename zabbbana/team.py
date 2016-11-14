class Team():

    def __init__(self, client, team_id):
        self.client  = client
        self.team_id = str(team_id)


    def list_players(self, team_id=None):
        """
            List a team's players
            http://developer.dribbble.com/v1/teams/members/
        """
        team_id             = str(team_id) if team_id is not None else self.team_id
        team_players        = self.client.get("/teams/{}/members".format(team_id))
        return team_players.json()


    def list_shots(self, team_id=None):
        """ List a team's shots
            http://developer.dribbble.com/v1/teams/shots/
        """
        team_id             = str(team_id) if team_id is not None else self.team_id
        team_shots          = self.client.get("/teams/{}/shots".format(team_id))
        return team_shots.json()
