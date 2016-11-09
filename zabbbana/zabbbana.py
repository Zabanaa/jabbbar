__author__ = "Karim Cheurfi"

API_ENDPOINT    = "https://api.dribbble.com/v1"
AUTH_ENDPOINT   = "https://dribbble.com/oauth/authorize"
SCOPE           = ['write', 'public', 'comment', 'upload']

class Zabbbana(object):

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, state=None, scope=SCOPE):
        self.client_id      = client_id
        self.client_secret  = client_secret
        self.redirect_uri   = redirect_uri
        self.state          = state
        self.scope          = "+".join(scope)

    def generate_auth_url(self):
        return "{}?client_id={}&redirect_uri={}&scope={}&state={}".format(AUTH_ENDPOINT, self.client_id,\
                self.redirect_uri, self.scope, self.state)

    def check_valid_state(self, state):
        """check that self.state matches state (return true)"""
        pass

    def get_access_token(self, auth_code):
        # send a token request using the code
        # extract the code from the response
        # set selt.access_token to the extracted token
        # return the effin token
        pass
