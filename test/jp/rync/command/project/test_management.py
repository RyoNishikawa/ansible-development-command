import unittest
import os
import shutil

from jp.rync.command.project.management import AnsibleProject


class TestAnsibleProject(unittest.TestCase):

    def setUp(self):
        self.delete_test_files()

    def tearDown(self):
        self.delete_test_files()

    def delete_test_files(self):
        test_dirs = [
            'test_project1',
            'test_project2'
        ]
        for path in test_dirs:
            if os.path.exists(path):
                shutil.rmtree(path)

    def test_create_project(self):
        """
        This command should be create the project directory.
        And then, create hosts and site.yml in project directory.
        """
        test_instance = AnsibleProject('test_project1')
        ref = test_instance.create_project()

        self.assertTrue(os.path.exists('test_project1'))
        self.assertTrue(os.path.exists('test_project1/hosts'))
        self.assertTrue(os.path.exists('test_project1/site.yml'))
        self.assertTrue(os.path.exists('test_project1/.ansible_project/project.json'))
        self.assertEqual(ref, 0)

    def test_create_roles(self):
        """
        Create directories and files that need the roles.
        """
        setup_instance = AnsibleProject('test_project2')
        setup_instance.create_project()

        os.chdir('test_project2')
        test_instance = AnsibleProject()
        ref = test_instance.create_role('test_role')

        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.assertTrue(os.path.exists('test_project2/roles'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role/tasks/main.yml'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role/vars/main.yml'))
        self.assertEqual(ref, 0)


