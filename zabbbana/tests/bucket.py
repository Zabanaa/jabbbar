import unittest
from .credentials import *
from zabbbana import Zabbbana
from zabbbana.bucket import Bucket

jordan = Zabbbana(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI,\
                  access_token=ACCESS_TOKEN, state="hello")
my_bucket = Bucket(jordan, 2754)

class BucketTest(unittest.TestCase):

    def setUp(self):
        self.bucket = Bucket(jordan, 2754)

    def test_get_details(self):
        details = self.bucket.get_details()
        self.assertIn('shots_count', details)

    def test_create_bucket(self):
        bucket_name         = "my new name"
        bucket_description  = "new cool bucket"
        post_bucket         = self.bucket.create(name=bucket_name, description=bucket_description)
        self.assertIn('created_at', post_bucket)

    def test_update_bucket(self):
        bucket_new_name = "bruv wagwan"
        response        = self.bucket.update(bucket_id=442460, name=bucket_new_name)
        self.assertEqual(bucket_new_name, response['name'])

if __name__ == "__main__":
    unittest.main()
