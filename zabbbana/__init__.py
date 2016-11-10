import requests as req

__author__ = "Karim Cheurfi"

API_ENDPOINT    = "https://api.dribbble.com/v1"
AUTH_ENDPOINT   = "https://dribbble.com/oauth/authorize"
OAUTH_ENDPOINT  = "https://dribbble.com/oauth/token"
SCOPE           = ['write', 'public', 'comment', 'upload']

class Zabbbana(object):

    API_ENDPOINT    = "https://api.dribbble.com/v1"

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, access_token=None, state=None, scope=SCOPE):
        self.client_id      = client_id
        self.client_secret  = client_secret
        self.redirect_uri   = redirect_uri
        self.state          = state
        self.scope          = "+".join(scope)
        self.access_token   = access_token

    @property
    def generate_auth_url(self):
        """ Generates a URL to the authorize endpoint used by dribbble to return a grant_code """
        return "{}?client_id={}&redirect_uri={}&scope={}&state={}".format(AUTH_ENDPOINT, self.client_id,\
                self.redirect_uri, self.scope, self.state)

    def get_access_token(self, auth_code=None):

        """ takes the grant code provided during Object.generate_auth_url() and makes a request to the dribbble api for
        an access token. Extracts it from the response and stores it a an instance variable"""

        oauth_params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': auth_code,
            'redirect_uri': self.redirect_uri
        }
        token_request       = req.post(OAUTH_ENDPOINT, data=oauth_params)
        token_response      = token_request.json()
        access_token        = token_response['access_token']
        self.access_token   = access_token
