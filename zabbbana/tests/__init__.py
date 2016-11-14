from zabbbana import Zabbbana
from .credentials import *

jordan = Zabbbana(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, state="myrandomkey",\
                  redirect_uri=REDIRECT_URI)


def test_generate_auth_url():
    expected_url = "https://dribbble.com/oauth/authorize?client_id={}&redirect_uri={}&scope={}&state={}"\
                    .format(jordan.client_id, jordan.redirect_uri, jordan.scope, jordan.state)
    auth_url     = jordan.generate_auth_url
    assert auth_url == expected_url
