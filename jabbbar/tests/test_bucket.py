from jabbbar.bucket import Bucket
from . import client

EXTERNAL_BUCKET_ID  = 2755
BUCKET_TO_UPDATE    = 442480
DEFAULT_SHOT_ID     = 471756
DEFAULT_BUCKET_ID   = 386137

test_bucket = Bucket(client, DEFAULT_BUCKET_ID)

def test_get_details():
    # Without ID (the instance bucket)
    response = test_bucket.get_details()
    assert 'shots_count' in response

    # With ID (another bucket)
    response = test_bucket.get_details(bucket_id=EXTERNAL_BUCKET_ID)
    assert 'shots_count' in response

def test_create_and_delete_bucket():
    bucket_name, bucket_description = ["my new name", "new cool bucket"]
    response            = test_bucket.create(name=bucket_name, description=bucket_description)
    assert 'created_at' in response

    response = test_bucket.delete(bucket_id=response['id'])
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_update_bucket():
    # Without ID (the instance bucket)
    bucket_new_name = "Jobs board for python developers"
    response        = test_bucket.update(name=bucket_new_name)
    assert bucket_new_name == response['name']

    # With ID (another bucket)
    bucket_new_name = "bruv wagwan"
    response        = test_bucket.update(bucket_id=BUCKET_TO_UPDATE, name=bucket_new_name)
    assert bucket_new_name == response['name']

def test_list_all_shots():
    # Without ID (the instance bucket)
    response    = test_bucket.list_shots()
    assert isinstance(response, list)

    # With Id (another bucket)
    response    = test_bucket.list_shots(bucket_id=EXTERNAL_BUCKET_ID)
    assert isinstance(response, list)

def test_add_shot():
    response    = test_bucket.add_shot(shot_id=DEFAULT_SHOT_ID)
    status_code = response.__dict__['status_code']
    assert status_code == 204

def test_remove_shot():
    response    = test_bucket.remove_shot(shot_id=DEFAULT_SHOT_ID)
    status_code = response.__dict__['status_code']
    assert status_code == 204
