from jabbbar import Project
from . import client
import time

DEFAULT_PROJECT_ID = 3

test_project = Project(client, DEFAULT_PROJECT_ID)

def test_get_details():

    time.sleep(1.5)
    response = test_project.get_details()
    assert response['id'] == test_project.project_id

    time.sleep(1.5)
    response = test_project.get_details(project_id=4)
    assert response['id'] == 4

def test_get_shots():
    time.sleep(1.5)
    response = test_project.get_shots()
    assert isinstance(response, list)

    time.sleep(1.5)
    response = test_project.get_shots(project_id=4)
    assert isinstance(response, list)
