from jabbbar import Jabbbar
from .credentials import *

client = Jabbbar(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, state="myrandomkey",\
                  redirect_uri=REDIRECT_URI)

def test_generate_auth_url():
    expected_url = "https://dribbble.com/oauth/authorize?client_id={}&redirect_uri={}&scope={}&state={}"\
                    .format(client.client_id, client.redirect_uri, client.scope, client.state)
    auth_url     = client.auth_url
    assert auth_url == expected_url
