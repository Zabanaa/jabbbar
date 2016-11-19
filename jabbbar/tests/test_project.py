from jabbbar import Project
from . import client, userless_client
import time

DEFAULT_PROJECT_ID = 3

test_project     = Project(client, DEFAULT_PROJECT_ID)
userless_project = Project(userless_client)

class TestProject():

    def test_get_details(self):

        # Get the instantiated project's details
        time.sleep(2)
        response = test_project.get_details()
        assert response['id'] == test_project.project_id

        # Get details for another project
        time.sleep(2)
        response = test_project.get_details(project_id=4)
        assert response['id'] == 4

    def test_get_shots(self):
        # Get shots for the instantiated project
        time.sleep(2)
        response = test_project.get_shots()
        assert isinstance(response, list)

        # Get shots for another project
        time.sleep(2)
        response = test_project.get_shots(project_id=4)
        assert isinstance(response, list)

class TestUserlessProject():

    def test_get_details(self):
        time.sleep(2)
        response = userless_project.get_details(project_id=4)
        assert response['id'] == 4

    def test_get_shots(self):
        time.sleep(2)
        response = userless_project.get_shots(project_id=4)
        assert isinstance(response, list)
