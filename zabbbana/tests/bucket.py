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

if __name__ == "__main__":
    unittest.main()
