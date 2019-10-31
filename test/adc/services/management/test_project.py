import unittest
import os
import shutil
import json

from adc.services.management.project import Project
from test.util.file import TestFile


class TestProject(unittest.TestCase):

    def setUp(self):
        self.delete_test_files()

    def tearDown(self):
        self.delete_test_files()

    def delete_test_files(self):
        test_dirs = [
            'test_project1',
            'test_project2',
            'test_project3'
        ]
        TestFile.delete_directories(test_dirs)

    def test_create_project(self):
        """
        This command should be create the project directory.
        And then, create hosts and site.yml in project directory.
        """
        test_instance = Project('test_project1')
        ref = test_instance.create_project()

        self.assertTrue(os.path.exists('test_project1'))
        self.assertTrue(os.path.exists('test_project1/hosts'))
        self.assertTrue(os.path.exists('test_project1/site.yml'))
        self.assertTrue(os.path.exists('test_project1/.ansible_project/project.json'))
        with open('test_project1/.ansible_project/project.json', 'r+') as f:
            project_conf = json.load(f)
            project_name = project_conf.get("project_name")
            self.assertEqual(project_name, 'test_project1')
        self.assertEqual(ref, 0)

    def test_create_roles(self):
        """
        Create directories and files that need the roles.
        """
        setup_instance = Project('test_project2')
        setup_instance.create_project()

        os.chdir('test_project2')
        test_instance = Project()
        ref = test_instance.create_role('test_role')

        os.chdir("..")

        self.assertTrue(os.path.exists('test_project2/roles'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role/tasks/main.yml'))
        self.assertTrue(os.path.exists('test_project2/roles/test_role/vars/main.yml'))
        self.assertEqual(ref, 0)

    def test_create_project_without_argument(self):
        """
        This commad should be create the project files when execute it without arguments.
        """
        os.mkdir('test_project3')
        os.chdir('test_project3')

        setup_instance = Project('.')
        ref = setup_instance.create_project()

        os.chdir('..')

        self.assertTrue(os.path.exists('test_project3/hosts'))
        self.assertTrue(os.path.exists('test_project3/site.yml'))
        self.assertTrue(os.path.exists('test_project3/.ansible_project/project.json'))
        with open('test_project3/.ansible_project/project.json', 'r+') as f:
            project_conf = json.load(f)
            project_name = project_conf.get("project_name")
            self.assertEqual(project_name, 'test_project3')
        self.assertEqual(ref, 0)
