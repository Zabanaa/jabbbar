import unittest
from zabbbana import Zabbbana
from zabbbana.project import Project
from zabbbana.tests import jordan

class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.project = Project(jordan,3)

    def test_get_details(self):
        response = self.project.get_details()
        self.assertEqual(response['id'], self.project.project_id)

        response = self.project.get_details(project_id=4)
        self.assertEqual(response['id'], 4)

    def test_get_shots(self):

        response = self.project.get_shots()
        self.assertIs(type(response), list)

if __name__ == "__main__":
    unittest.main()
