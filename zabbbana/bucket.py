from zabbbana import Zabbbana as zbn
import requests as req

class Bucket(zbn):

    def __init__(self, inst, bucket_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.bucket_id = bucket_id

    def get_details(self):
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        bucket_details = req.get("{}/buckets/{}", headers=headers).format(zbn.API_ENDPOINT, self.bucket_id)
