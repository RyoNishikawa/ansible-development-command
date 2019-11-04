import os
import unittest

from adc.models.setting import ProjectConfig
from test.util.file import TestFile


class TestSetting(unittest.TestCase):

    _directory_name_test_project = 'test_project'
    _project_config_directory = '.ansible_project'

    def setUp(self) -> None:
        TestFile.delete_directory(self._directory_name_test_project)
        TestFile.create_blank_directory(self._directory_name_test_project)

    def tearDown(self) -> None:
        TestFile.delete_directory(self._directory_name_test_project)

    def test_project_config_generate(self):
        ProjectConfig.generate(self._directory_name_test_project)
        os.chdir(self._directory_name_test_project)
        ProjectConfig.load()

        self.assertEqual('test_project', ProjectConfig.get(ProjectConfig.DICT_KEY_PROJECT_NAME))
        self.assertEqual('/etc/ansible/hosts', ProjectConfig.get(ProjectConfig.DICT_KEY_GLOBAL_INVENTORY_FILE_PATH))
        self.assertEqual('./hosts', ProjectConfig.get(ProjectConfig.DICT_KEY_PROJECT_INVENTORY_FILE_PATH))
