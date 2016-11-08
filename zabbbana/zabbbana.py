__author__ = "Karim Cheurfi"

class Zabbbana(object):

    def __init__(self, client_id, client_secret, redirect_uri, scope, state):
        self.client_id      = client_id
        self.client_secret  = client_secret
        self.redirect_uri   = redirect_uri
        self.access_token   = None
        self.state          = state
        self.scope          = self.generate_scope(scope)

    def generate_auth_url(self):
        """return dribbble.com/authorize?client_id&client_secret&scope&state"""
        pass


    def generate_scope(self, scope_list):
        # loop through the list and return a string joined with + signs
        pass


    def check_valid_state(self, state):
        """check that self.state matches state (return true)"""
        pass

    def get_access_token(self, auth_code):
        # send a token request using the code
        # extract the code from the response
        # set selt.access_token to the extracted token
        # return the effin token
        pass
