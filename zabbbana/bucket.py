from zabbbana import Zabbbana as zbn
import requests as req

class Bucket(zbn):

    def __init__(self, inst, bucket_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.bucket_id = bucket_id

    def get_details(self):
        bucket_request = req.get("{}/buckets/{}".format(zbn.API_ENDPOINT, self.bucket_id), headers=self.auth_header)
        details = bucket_request.json()
        return details

    def create(self, name=None, description=None):
        bucket_data     = {'name': name, 'description': description}
        post_bucket     = req.post("{}/buckets".format(zbn.API_ENDPOINT), headers=self.auth_header, data=bucket_data)
        response        = post_bucket.json()
        return response

    def update(self, bucket_id=None, name=None, description=None):
        bucket_data     = {'name': name, 'description': description}
        update_bucket   = req.put("{}/buckets/{}".format(zbn.API_ENDPOINT, bucket_id), headers=self.auth_header,\
                                  data=bucket_data)
        response        = update_bucket.json()
        return response

    def delete(self, bucket_id=None):
        response  = req.delete("{}/buckets/{}".format(zbn.API_ENDPOINT, bucket_id), headers=self.auth_header)
        return response

    def list_shots(self,bucket_id=None):
        if bucket_id:
            bucket_id = bucket_id
        else:
            bucket_id = self.bucket_id

        shots_list = req.get("{}/buckets/{}/shots".format(zbn.API_ENDPOINT, bucket_id), headers=self.auth_header)
        response   = shots_list.json()
        return response

    def add_shot(self, shot_id=None):

        """Adds a shot to the current bucket, we don't return the json response so we can access the status code in the
        headers"""

        shot_data = {'shot_id': shot_id}
        push_shot = req.put("{}/buckets/{}/shots".format(zbn.API_ENDPOINT, self.bucket_id), headers=self.auth_header,\
                            data=shot_data)
        return push_shot
