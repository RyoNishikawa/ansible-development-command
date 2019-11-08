import unittest
import os
import json
import tempfile

from adc.services.management.project import Project
from test.util.file import TestFile


class TestProject(unittest.TestCase):

    file_name_test_create_project = 'test_create_project'
    file_name_test_create_roles = 'test_create_roles'
    file_name_test_create_project_without_argument = 'test_create_project_without_argument'

    @classmethod
    def setUpClass(cls) -> None:
        cls.delete_test_files()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @classmethod
    def delete_test_files(cls):
        test_dirs = [
            cls.file_name_test_create_project,
            cls.file_name_test_create_roles,
            cls.file_name_test_create_project_without_argument
        ]
        TestFile.delete_directories(test_dirs)

    def test_create_project(self):
        """
        This command should be create the project directory.
        And then, create hosts and site.yml in project directory.
        """
        with tempfile.TemporaryDirectory() as td:
            os.chdir(td)
            test_instance = Project(self.file_name_test_create_project)
            ref = test_instance.create_project()

            self.assertTrue(os.path.exists(self.file_name_test_create_project))
            self.assertTrue(os.path.exists('{0}/hosts'.format(self.file_name_test_create_project)))
            self.assertTrue(os.path.exists('{0}/site.yml'.format(self.file_name_test_create_project)))
            self.assertTrue(os.path.exists('{0}/.ansible_project/project.json'.format(self.file_name_test_create_project)))
            with open('{0}/.ansible_project/project.json'.format(self.file_name_test_create_project), 'r+') as f:
                project_conf = json.load(f)
                project_name = project_conf.get("project_name")
                self.assertEqual(project_name, self.file_name_test_create_project)
            self.assertEqual(ref, 0)

    def test_create_roles(self):
        """
        Create directories and files that need the roles.
        """
        with tempfile.TemporaryDirectory() as td:
            os.chdir(td)
            setup_instance = Project(self.file_name_test_create_roles)
            setup_instance.create_project()

            print(os.getcwd())
            os.chdir(self.file_name_test_create_roles)
            test_instance = Project()
            ref = test_instance.create_role('test_role')

            os.chdir("..")

            self.assertTrue(os.path.exists('{0}/roles'.format(self.file_name_test_create_roles)))
            self.assertTrue(os.path.exists('{0}/roles/test_role'.format(self.file_name_test_create_roles)))
            self.assertTrue(os.path.exists('{0}/roles/test_role/tasks/main.yml'.format(self.file_name_test_create_roles)))
            self.assertTrue(os.path.exists('{0}/roles/test_role/vars/main.yml'.format(self.file_name_test_create_roles)))
            self.assertEqual(ref, 0)

    def test_create_project_without_argument(self):
        """
        This commad should be create the project files when execute it without arguments.
        """
        with tempfile.TemporaryDirectory() as td:
            os.chdir(td)
            os.mkdir(self.file_name_test_create_project_without_argument)
            os.chdir(self.file_name_test_create_project_without_argument)

            setup_instance = Project('.')
            ref = setup_instance.create_project()

            os.chdir('..')

            self.assertTrue(os.path.exists('{0}/hosts'.format(self.file_name_test_create_project_without_argument)))
            self.assertTrue(os.path.exists('{0}/site.yml'.format(self.file_name_test_create_project_without_argument)))
            self.assertTrue(os.path.exists('{0}/.ansible_project/project.json'.format(self.file_name_test_create_project_without_argument)))
            with open('{0}/.ansible_project/project.json'.format(self.file_name_test_create_project_without_argument), 'r+') as f:
                project_conf = json.load(f)
                project_name = project_conf.get("project_name")
                self.assertEqual(project_name, self.file_name_test_create_project_without_argument)
            self.assertEqual(ref, 0)
