import os
import json
import re

from typing import Dict


class ProjectConfig:
    # To store directory for Project file.
    _FIX_PARAMETER_BASE_DIRECTORY_PATH: str = 'ansible_project'
    # Project file path.
    _FIX_PARAMETER_PROJECT_FILE_NAME: str = 'project.json'

    # Project configuration key for project name.
    _DICT_KEY_PROJECT_NAME = 'project_name'

    # Project configuration keys.
    # global inventory file path
    _DICT_KEY_GLOBAL_INVENTORY_FILE_PATH: str = 'global_inventory_file_path'
    # project inventory file path
    _DICT_KEY_PROJECT_INVENTORY_FILE_PATH: str = 'project_inventory_file_path'

    # Project configuration values.
    # global inventory file path
    _DICT_VALUE_GLOBAL_INVENTORY_FILE_PATH: str = '/etc/ansible/hosts'
    # project inventory file path
    _DICT_VALUE_PROJECT_INVENTORY_FILE_PATH: str = './hosts'

    # Project configuration dictionary for generate method.
    _PROJECT_CONFIG_DICT_FOR_GENERATE: Dict[str, str] = {
        _DICT_KEY_GLOBAL_INVENTORY_FILE_PATH: _DICT_VALUE_GLOBAL_INVENTORY_FILE_PATH,
        _DICT_KEY_PROJECT_INVENTORY_FILE_PATH: _DICT_VALUE_PROJECT_INVENTORY_FILE_PATH
    }

    items: Dict[str, str]

    @classmethod
    def load(cls):
        if os.path.exists(cls._FIX_PARAMETER_BASE_DIRECTORY_PATH):
            with open(cls._FIX_PARAMETER_BASE_DIRECTORY_PATH, 'r+') as f:
                cls.items = json.load(f)

    @classmethod
    def generate(cls, project_name: str):
        os.mkdir('{0}/{1}'.format(project_name, cls._FIX_PARAMETER_BASE_DIRECTORY_PATH))
        with open(
                '{0}/{1}/{2}'.format(
                    project_name,
                    cls._FIX_PARAMETER_BASE_DIRECTORY_PATH,
                    cls._FIX_PARAMETER_BASE_DIRECTORY_PATH), 'w'
        ) as f:
            if project_name is '.':
                m = re.search(r'^.*/(.*)$', os.getcwd())
                project_name = m.group(1)
            default_settings = {cls._DICT_KEY_PROJECT_NAME: project_name}
            default_settings.update(cls._PROJECT_CONFIG_DICT_FOR_GENERATE)
            json.dump(default_settings, f)

    @classmethod
    def get(cls, key: str) -> str:
        return cls.items.get(key)

    @classmethod
    def items(cls) -> Dict[str, str]:
        return cls.items
