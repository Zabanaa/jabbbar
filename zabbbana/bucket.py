class Bucket():

    def __init__(self, client, bucket_id=None):
        self.client = client
        self.bucket_id = bucket_id

    def get_details(self, bucket_id=None):

        """ Retrieves information about either the current Bucket (if no bucket_id is passed)
            or the one that matches the passed bucket_id
            http://developer.dribbble.com/v1/buckets/#get-a-bucket
        """
        bucket_id   = bucket_id if bucket_id is not None else self.bucket_id
        bucket_details = self.client.GET('/buckets/{}'.format(bucket_id))
        return bucket_details.json()

    def create(self, name=None, description=None):

        """
            Creates a new bucket
            http://developer.dribbble.com/v1/buckets/#create-a-bucket
        """

        bucket_data     = {'name': name, 'description': description}
        post_bucket     = self.client.POST("/buckets", data=bucket_data)
        return post_bucket.json()

    def update(self, bucket_id=None, name=None, description=None):

        """ Update the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to update it
            http://developer.dribbble.com/v1/buckets/#update-a-bucket
        """

        bucket_id = bucket_id if bucket_id is not None else self.bucket_id
        bucket_data     = {'name': name, 'description': description}
        update_bucket   = self.client.PUT("/buckets/{}".format(bucket_id), data=bucket_data)
        return update_bucket.json()

    def delete(self, bucket_id=None):

        """ Deletes the current bucket or the one that matches the passed bucket_id
            Please note that the user must own the bucket to delete it
            http://developer.dribbble.com/v1/buckets/#delete-a-bucket
        """
        bucket_id       = bucket_id or self.bucket_id
        delete_response = self.client.DELETE('/buckets/{}'.format(bucket_id))
        return delete_response

    def list_shots(self,bucket_id=None):

        """
            Lists all the shots within a the current (or designated) bucket
            http://developer.dribbble.com/v1/buckets/shots/#list-shots-for-a-bucket
        """

        bucket_id       = bucket_id or self.bucket_id
        shots_list      = self.client.GET("/buckets/{}/shots".format(bucket_id))
        return shots_list.json()

    def add_shot(self, shot_id):

        """Adds a shot to the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to add shots to it.
           http://developer.dribbble.com/v1/buckets/shots/#add-a-shot-to-a-bucket
        """

        shot_data                = {'shot_id': shot_id}
        new_shot_response        = self.client.PUT("/buckets/{}/shots".format(self.bucket_id), data=shot_data)
        return new_shot_response

    def remove_shot(self, shot_id):

        """Removes a shot from the current bucket, we return the raw response so we can test the status code
           Please note that the current user must own the bucket to remove shots from it.
           http://developer.dribbble.com/v1/buckets/shots/#remove-a-shot-from-a-bucket
        """

        shot_data                    = {'shot_id': shot_id}
        delete_shot_response         = self.client.DELETE("/buckets/{}/shots".format(self.bucket_id))
        return delete_shot_response
