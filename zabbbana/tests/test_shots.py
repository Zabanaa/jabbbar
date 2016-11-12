from zabbbana.shots import Shots
from . import jordan

test_shots = Shots(jordan)

DEFAULT_SHOT_ID      = 471756
DEFAULT_QUERY_PARAMS = {
    'list': 'debuts',
    'timeframe': 'month',
    'date': '20151121',
    'sort': 'comments'
}
DEFAULT_UPLOAD_PARAMS = {
    'title': 'Bruv new shot",
    'image': path_to_image,
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
