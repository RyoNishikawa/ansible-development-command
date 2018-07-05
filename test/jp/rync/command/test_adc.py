import unittest
import sys

import jp.rync.command.adc


class TestAnsibleDevelopmentCommand(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_params_with_init(self):
        parse = jp.rync.command.adc.AnsibleDevelopmentCommand.parser(['init'])
        self.assertTrue(parse.init)

    def test_help(self): pass

    def test_create_project(self): pass
