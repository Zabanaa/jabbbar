import os
from zabbbana.shots import Shots
from . import jordan

test_shots = Shots(jordan)
PATH_TO_IMG = os.path.dirname(__file__)

DEFAULT_SHOT_ID      = 471756
DEFAULT_QUERY_PARAMS = {
    'list': 'debuts',
    'timeframe': 'month',
    'date': '20151121',
    'sort': 'comments'
}
DEFAULT_UPLOAD_PARAMS = {
    'title': 'Bruv new shot',
    'image': os.path.join(PATH_TO_IMG, 'sample.png'),
    'description': 'Testing shot uploading on this ting',
    'tags': ['mad ting'],
    'team_id': None,
    'rebound_source_id': None
}

def test_list_all():

    response = test_shots.list_all(DEFAULT_QUERY_PARAMS)
    assert isinstance(response, list)

def test_get_one():
    response = test_shots.get_one(DEFAULT_SHOT_ID)
    assert response['id'] == DEFAULT_SHOT_ID

    response = test_shots.get_one(1209392210321321)
    assert 'Not found.' in response['message']

def test_upload_shot():

    response = test_shots.upload(DEFAULT_UPLOAD_PARAMS)
    pass

def test_update_shot():
    pass

def test_delete_shot():
    pass


