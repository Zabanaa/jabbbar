from zabbbana import Zabbbana as zbn
import requests as req

class Bucket(zbn):

    MAIN_ENDPOINT = "{}/buckets".format(zbn.API_ENDPOINT)

    def __init__(self, inst, bucket_id):
        zbn.__init__(self, client_id=inst.client_id, client_secret=inst.client_secret, access_token=inst.access_token)
        self.bucket_id = bucket_id

    def get_details(self, bucket_id=None):

        """ Retrieves information about either the current Bucket (if no bucket_id is passed)
            or the one that matches the passed bucket_id
        """

        if bucket_id:
            bucket_id = bucket_id
        else:
            bucket_id = self.bucket_id

        bucket_request = req.get("{}/{}".format(self.MAIN_ENDPOINT, bucket_id), headers=self.auth_header)
        details = bucket_request.json()
        return details

    def create(self, name=None, description=None):

        """ Creates a new bucket """

        bucket_data     = {'name': name, 'description': description}
        post_bucket     = req.post(self.MAIN_ENDPOINT, headers=self.auth_header, data=bucket_data)
        response        = post_bucket.json()
        return response

    def update(self, bucket_id=None, name=None, description=None):

        """ Update the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to update it
        """

        if bucket_id:
            bucket_id = bucket_id
        else:
            bucket_id = self.bucket_id

        bucket_data     = {'name': name, 'description': description}
        update_bucket   = req.put("{}/{}".format(self.MAIN_ENDPOINT, bucket_id), headers=self.auth_header, data=bucket_data)
        response        = update_bucket.json()
        return response

    def delete(self, bucket_id=None):

        """ Deletes the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to delete it
        """
        if bucket_id:
            bucket_id = bucket_id
        else:
            bucket_id = self.bucket_id

        response  = req.delete("{}/{}".format(self.MAIN_ENDPOINT, bucket_id), headers=self.auth_header)
        return response

    def list_shots(self,bucket_id=None):

        """ Lists all the shots within a the current (or designated) bucket """

        if bucket_id:
            bucket_id = bucket_id
        else:
            bucket_id = self.bucket_id

        shots_list = req.get("{}/{}/shots".format(self.MAIN_ENDPOINT, bucket_id), headers=self.auth_header)
        response   = shots_list.json()
        return response

    def add_shot(self, shot_id):

        """Adds a shot to the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to add shots to it.
        """

        shot_data = {'shot_id': shot_id}
        push_shot = req.put("{}/{}/shots".format(self.MAIN_ENDPOINT, self.bucket_id), headers=self.auth_header, data=shot_data)
        return push_shot

    def remove_shot(self, shot_id):

        """Removes a shot from the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to remove shots from it.
        """

        shot_data = {'shot_id': shot_id}
        push_shot = req.delete("{}/{}/shots".format(self.MAIN_ENDPOINT, self.bucket_id), headers=self.auth_header, data=shot_data)
        return push_shot
