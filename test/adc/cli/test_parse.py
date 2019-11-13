import unittest
import sys

from lib.adc.cli.parse import CommandParse


class TestAnsibleDevelopmentCommand(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_init_subcommand(self):
        sys.argv = ['adc', 'init']
        params = CommandParse.parser()
        print(params)
        self.assertIsNone(params.init_project_name)

    def test_init_subcommand_with_arguments(self):
        sys.argv = ['adc', 'init', 'test_project']
        params = CommandParse.parser()
        print(params)
        self.assertEqual(params.init_project_name, 'test_project')

    def test_list_subcommand_with_hosts_subcommand(self):
        sys.argv = ['adc', 'list', 'hosts']
        params = CommandParse.parser()
        print(params)
        self.assertEqual(params.list_hosts, True)

    def test_create_subcommand_with_roles_subcommand(self):
        sys.argv = ['adc', 'create', 'roles', 'test_role']
        params = CommandParse.parser()
        print(params)
        self.assertEqual(params.create_role_name, ['test_role'])

    def test_roles_subcommand_with_create_option_with_vars_option(self): pass

    def test_roles_subcommand_with_create_option_with_files_option(self): pass

    def test_roles_subcommand_with_create_option_with_templates_option(self): pass


