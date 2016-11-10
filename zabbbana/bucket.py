from zabbbana import Zabbbana as zbn
import requests as req

class Bucket(zbn):

    def __init__(self, client, bucket_id):
        zbn.__init__(self, client.client_id, client.client_secret, client.access_token)
        self.bucket_id = bucket_id

    def get_details(self):
        print(zbn.API_ENDPOINT)
