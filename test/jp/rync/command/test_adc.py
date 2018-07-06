import unittest
import sys

import jp.rync.command.adc


class TestAnsibleDevelopmentCommand(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_init_subcommand(self):
        sys.argv = ['adc', 'init']
        params = jp.rync.command.adc.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertIsNone(params.init_project_name)

    def test_init_subcommand_with_arguments(self):
        sys.argv = ['adc', 'init', 'test_project']
        params = jp.rync.command.adc.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.init_project_name, 'test_project')

    def test_roles_subcommand_with_create_option(self):
        sys.argv = ['adc', 'roles', '--create', 'test_role']
        params = jp.rync.command.adc.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.create_role_name, 'test_role')

    def test_roles_subcommand_with_create_omit_option(self):
        sys.argv = ['adc', 'roles', '-c', 'test_role']
        params = jp.rync.command.adc.AnsibleDevelopmentCommand.parser()
        print(params)
        self.assertEqual(params.create_role_name, 'test_role')

