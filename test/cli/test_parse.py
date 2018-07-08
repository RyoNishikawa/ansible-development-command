import unittest
import sys

from adc.cli import AnsibleDevelopCommand


class TestAnsibleDevelopmentCommand(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_init_subcommand(self):
        sys.argv = ['adc', 'init']
        params = lib.jp.rync.command.ansible_develop_command.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertIsNone(params.init_project_name)

    def test_init_subcommand_with_arguments(self):
        sys.argv = ['adc', 'init', 'test_project']
        params = lib.jp.rync.command.ansible_develop_command.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.init_project_name, 'test_project')

    def test_roles_subcommand_with_create_option(self):
        sys.argv = ['adc', 'roles', '--create', 'test_role']
        params = lib.jp.rync.command.ansible_develop_command.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.create_role_name, 'test_role')

    def test_roles_subcommand_with_create_omit_option(self):
        sys.argv = ['adc', 'roles', '-c', 'test_role']
        params = lib.jp.rync.command.ansible_develop_command.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.create_role_name, 'test_role')

    def test_roles_subcommand_with_create_option_with_vars_option(self): pass

    def test_roles_subcommand_with_create_option_with_files_option(self): pass

    def test_roles_subcommand_with_create_option_with_templates_option(self): pass


