class Shots():

    def __init__(self, client):
        self.client = client

    def list_all(self, params):

        """
            Retrieve a list of all uploaded shots on the site
            http://developer.dribbble.com/v1/shots/#list-shots
        """

        shots = self.client.GET("/shots")
        return shots.json()

    def get_one(self, shot_id):

        """
            Get details for a specific shot
            http://developer.dribbble.com/v1/shots/#get-a-shot
        """

        shot_info   = self.client.GET("/shots/{}".format(shot_id))
        return shot_info.json()

    def upload(self, shot_data):

        """
            Uploads a shot to the user's account (the user must be authenticated with the upload scope,
        he/she also must be a drafted player
            http://developer.dribbble.com/v1/shots/#create-a-shot
        """

        upload_shot = self.client.POST("/shots", data=shot_data)
        return upload_shot

    def update(self, shot_id, shot_data):

        """
            Update information about a shot
            http://developer.dribbble.com/v1/shots/#update-a-shot
        """
        pass

    def delete(self, shot_id):

        """
            Delete a specific shot
            http://developer.dribbble.com/v1/shots/#delete-a-shot
        """

        pass
