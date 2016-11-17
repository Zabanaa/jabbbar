class Project():

    def __init__(self, client, project_id=None):
        self.client     = client
        self.project_id = project_id

    def get_details(self, project_id=None):

        """
            Get information about a specific project
            http://developer.dribbble.com/v1/projects/#get-a-project
        """

        project_id      = project_id if project_id is not None else self.project_id
        project_details = self.client.GET("/projects/{}".format(project_id))
        return project_details.json()

    def get_shots(self, project_id=None):

        """
            Retrieves a list of all shots that are part of this project
            http://developer.dribbble.com/v1/projects/shots/#list-shots-for-a-project
        """

        project_id      = project_id if project_id is not None else self.project_id
        shots           = self.client.GET("/projects/{}/shots".format(project_id))
        return shots.json()
