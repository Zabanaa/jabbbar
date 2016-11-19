from jabbbar import Team
import time
from . import client, userless_client

DEFAULT_TEAM_ID = "Creativedash"
test_team       = Team(client, DEFAULT_TEAM_ID)
userless_team   = Team(userless_client)

class TestTeam():

    def test_list_players(self):
        # List all the players who are part of the instanciated team
        time.sleep(2)
        response        = test_team.list_players()
        assert isinstance(response, list)

        # List all the players who are part of another team
        time.sleep(2)
        response        = test_team.list_players(team_name="ueno")
        assert isinstance(response, list)


    def test_list_shots(self):
        # List all the shots published by the instanciated team
        time.sleep(2)
        response        = test_team.list_shots()
        assert isinstance(response, list)

        # List all the shots published by another team
        time.sleep(2)
        response        = test_team.list_shots(team_name="ueno")
        assert isinstance(response, list)

class TestUserlessTeam():

    def test_list_players(self):
        time.sleep(2)
        response        = userless_team.list_players(team_name="ueno")
        assert isinstance(response, list)


    def test_list_shots(self):
        time.sleep(2)
        response        = userless_team.list_shots(team_name="ueno")
        assert isinstance(response, list)
