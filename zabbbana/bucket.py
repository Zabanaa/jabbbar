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
        bucket_id   = bucket_id if bucket_id is not None else self.bucket_id
        endpoint    = "{}/{}".format(self.MAIN_ENDPOINT, bucket_id)
        bucket_details = req.get(endpoint, headers=self.auth_header)
        return bucket_details.json()

    def create(self, name=None, description=None):

        """ Creates a new bucket """

        bucket_data     = {'name': name, 'description': description}
        endpoint        = self.MAIN_ENDPOINT
        post_bucket     = req.post(endpoint, headers=self.auth_header, data=bucket_data)
        return post_bucket.json()

    def update(self, bucket_id=None, name=None, description=None):

        """ Update the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to update it
        """

        bucket_id = bucket_id if bucket_id is not None else self.bucket_id
        bucket_data     = {'name': name, 'description': description}
        endpoint        = "{}/{}".format(self.MAIN_ENDPOINT, bucket_id)
        update_bucket   = req.put(endpoint, headers=self.auth_header, data=bucket_data)
        return update_bucket.json()

    def delete(self, bucket_id=None):

        """ Deletes the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to delete it
        """
        bucket_id       = bucket_id or self.bucket_id
        endpoint        = "{}/{}".format(self.MAIN_ENDPOINT, bucket_id)
        delete_response = req.delete(endpoint, headers=self.auth_header)
        return delete_response

    def list_shots(self,bucket_id=None):

        """ Lists all the shots within a the current (or designated) bucket """

        bucket_id       = bucket_id or self.bucket_id
        endpoint        = "{}/{}/shots".format(self.MAIN_ENDPOINT, bucket_id)
        shots_list      = req.get(endpoint, headers=self.auth_header)
        return shots_list.json()

    def add_shot(self, shot_id):

        """Adds a shot to the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to add shots to it.
        """

        shot_data                = {'shot_id': shot_id}
        endpoint                 = "{}/{}/shots".format(self.MAIN_ENDPOINT, self.bucket_id)
        new_shot_response        = req.put(endpoint, headers=self.auth_header, data=shot_data)
        return new_shot_response

    def remove_shot(self, shot_id):

        """Removes a shot from the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to remove shots from it.
        """

        shot_data                    = {'shot_id': shot_id}
        endpoint                     = "{}/{}/shots".format(self.MAIN_ENDPOINT, self.bucket_id)
        delete_shot_response         = req.delete(endpoint, headers=self.auth_header, data=shot_data)
        return delete_shot_response
