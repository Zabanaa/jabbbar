import unittest
from .credentials import *
from zabbbana import Zabbbana

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.api = Zabbbana(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI
        )

if __name__ == "__main__":
    unittest.main()
