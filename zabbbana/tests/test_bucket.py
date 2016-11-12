import unittest
from zabbbana import Zabbbana
from zabbbana.bucket import Bucket
from zabbbana.tests import jordan

EXTERNAL_BUCKET_ID = 2755
BUCKET_TO_UPDATE   = 442480
DEFAULT_SHOT_ID     = 471756

class BucketTest(unittest.TestCase):

    def setUp(self):
        self.bucket = Bucket(jordan, 386137)

    def test_get_details(self):
        # Without ID (the instance bucket)
        response = self.bucket.get_details()
        self.assertIn('shots_count', response)

        # With ID (another bucket)
        response = self.bucket.get_details(bucket_id=EXTERNAL_BUCKET_ID)
        self.assertIn('shots_count', response)

    def test_create_bucket(self):
        bucket_name         = "my new name"
        bucket_description  = "new cool bucket"
        response            = self.bucket.create(name=bucket_name, description=bucket_description)
        self.assertIn('created_at', response)
        self.bucket.delete(bucket_id=response['id']) # Immediately delete the created bucket to avoid bloat

    def test_update_bucket(self):
        # Without ID (the instance bucket)
        bucket_new_name = "Jobs board for python developers"
        response        = self.bucket.update(name=bucket_new_name)
        self.assertEqual(bucket_new_name, response['name'])

        # With ID (another bucket)
        bucket_new_name = "bruv wagwan"
        response        = self.bucket.update(bucket_id=BUCKET_TO_UPDATE, name=bucket_new_name)
        self.assertEqual(bucket_new_name, response['name'])

    def delete_bucket(self):
        response    = self.bucket.delete(bucket_id=442503)
        self.assertEqual(204, response.__dict__['status_code'])

    def test_list_all_shots(self):
        # Without ID (the instance bucket)
        response    = self.bucket.list_shots()
        self.assertIs(type(response), list)

        # With Id (another bucket)
        response    = self.bucket.list_shots(bucket_id=EXTERNAL_BUCKET_ID)
        self.assertIs(type(response), list)

    def test_add_shot(self):
        response    = self.bucket.add_shot(shot_id=DEFAULT_SHOT_ID)
        self.assertEqual(204, response.__dict__['status_code'])

    def test_remove_shot(self):
        response    = self.bucket.remove_shot(shot_id=DEFAULT_SHOT_ID)
        self.assertEqual(204, response.__dict__['status_code'])

if __name__ == "__main__":
    unittest.main()
