import requests as req

__author__ = "Karim Cheurfi"

API_URL         = "https://api.dribbble.com/v1"
AUTH_ENDPOINT   = "https://dribbble.com/oauth/authorize"
OAUTH_ENDPOINT  = "https://dribbble.com/oauth/token"
SCOPE           = ['write', 'public', 'comment', 'upload']

class Jabbbar(object):

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, client_token=None, access_token=None, state=None, scope=SCOPE):
        self.client_id          = client_id
        self.client_secret      = client_secret
        self.redirect_uri       = redirect_uri
        self.state              = state
        self.scope              = "+".join(scope)
        self.access_token       = access_token
        self.auth_header        = {'Authorization': 'Bearer {}'.format(self.access_token)}
        self.client_token       = client_token
        self.userless           = not bool(self.access_token) # Userless if no access_token is passed

    @property
    def auth_url(self):

        """ Generates a URL to the authorize endpoint used by dribbble to return a grant_code """

        return "{}?client_id={}&redirect_uri={}&scope={}&state={}".format(AUTH_ENDPOINT, self.client_id,\
                self.redirect_uri, self.scope, self.state)

    def set_access_token(self, auth_code=None):

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

    def _create_request_url(self, resource_url):
        return "{api_endpoint}{resource_url}".format(api_endpoint=API_URL, resource_url=resource_url)

    def GET(self, resource_endpoint, query_params={}):
        url         = self._create_request_url(resource_endpoint)
        params = query_params.copy() # Copy the query params object so we can append the credentials to it

        if self.userless:
            params['access_token'] = self.client_token
            return req.get(url, params=params)
        else:
            return req.get(url, headers=self.auth_header)

    def POST(self, resource_endpoint, data={}):
        url         = self._create_request_url(resource_endpoint)
        return req.post(url, headers=self.auth_header, data=data)

    def PUT(self, resource_endpoint, data={}):
        url         = self._create_request_url(resource_endpoint)
        return req.put(url, headers=self.auth_header, data=data)

    def DELETE(self, resource_endpoint):
        url         = self._create_request_url(resource_endpoint)
        return req.delete(url, headers=self.auth_header)
