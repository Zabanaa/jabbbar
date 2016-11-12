from zabbbana.project import Project
from . import jordan

test_project = Project(jordan,3)

def test_get_details():
    response = test_project.get_details()
    assert response['id'] == test_project.project_id

    response = test_project.get_details(project_id=4)
    assert response['id'] == 4

def test_get_shots():
    response = test_project.get_shots()
    assert isinstance(response, list)

    respone = test_project.get_shots(project_id=4)
    assert isinstance(response, list)
