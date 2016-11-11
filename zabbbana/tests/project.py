import unittest
from zabbbana import Zabbbana
from zabbbana.project import Project
from zabbbana.tests import jordan

class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.project = Project(jordan)

    def test_get_details(self):
        details = self.project.get_details(project_id=3)
        self.assertEqual(details['id'], 3)

if __name__ == "__main__":
    unittest.main()
