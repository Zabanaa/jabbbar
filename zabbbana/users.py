from zabbbana import Zabbbana as zbn
import requests as req


class User(zbn):

    MAIN_ENDPOINT = "{}/users".format(zbn.API_ENDPOINT)

    def __init__(self, inst):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)

    # get user
    # list authenticated user
    # list bucket
    # list authenticated users bucket
    # list shot likes
    # list shot likes for authed user
    # list projects
    # list projects for authed user
    # list shots
    # list shots for authed user
    # list teams
    # list teams for authed user
    # do the followers thing as well

