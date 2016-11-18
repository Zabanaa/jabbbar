import os
from jabbbar import Jabbbar

if 'CLIENT_ID' in os.environ and 'CLIENT_SECRET' in os.environ and 'ACCESS_TOKEN' in os.environ:
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
else:
    try:
        from jabbbar.tests.credentials import *
    except ImportError:
        print("Please create a credendtials.py file in this package, based upon credentials.example.py")

REDIRECT_URI = "http://localhost:3000"

client = Jabbbar(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, state="myrandomkey",\
                  redirect_uri=REDIRECT_URI)

def test_generate_auth_url():
    expected_url = "https://dribbble.com/oauth/authorize?client_id={}&redirect_uri={}&scope={}&state={}"\
                    .format(client.client_id, client.redirect_uri, client.scope, client.state)
    auth_url     = client.auth_url
    assert auth_url == expected_url
