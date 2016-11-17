class Team():

    def __init__(self, client, team_name=None):
        self.client     = client
        self.team_name  = str(team_name)


    def list_players(self, team_name=None):
        """
            List a team's players
            http://developer.dribbble.com/v1/teams/members/
        """
        team_name               = str(team_name) if team_name is not None else self.team_name
        team_players            = self.client.GET("/teams/{}/members".format(team_name))
        return team_players.json()


    def list_shots(self, team_name=None):
        """ List a team's shots
            http://developer.dribbble.com/v1/teams/shots/
        """
        team_name               = str(team_name) if team_name is not None else self.team_name
        team_shots              = self.client.GET("/teams/{}/shots".format(team_name))
        return team_shots.json()
