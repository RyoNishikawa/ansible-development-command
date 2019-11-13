import os
import json

from typing import List

from adc.models.setting import ProjectConfig


class Project:

    # Project name.
    _project_name: str = ""

    _PROJECT_FILE_PATH: str = ".ansible_project/project.json"

    # Check the project existing.
    _is_in_project: bool = False

    def __init__(self, project_name: str = ""):
        """
        Constructor.
        :param project_name: Project name.
        """

        self._is_in_project = os.path.exists(self._PROJECT_FILE_PATH)
        if self._is_in_project:
            with open(self._PROJECT_FILE_PATH, 'r+') as f:
                project_conf = json.load(f)
                project_name = project_conf.get("project_name")

        if project_name is "":
            project_name = "."

        self._project_name = project_name

    def create_project(self) -> int:
        """
        Create the project directory, hosts file and site.yml.
        Return status code.
        That is following to mean:
          0  : success
          1  : validation failed. (Exists ansible project file.)
          2  : validation failed. (Don't specify project name)
        :return: status code.
        """
        if self._is_in_project:
            return 1

        if self._project_name == "":
            return 2

        if self._project_name is not ".":
            os.mkdir("{0}".format(self._project_name))
        with open('{0}/hosts'.format(self._project_name), 'w') as writer: pass
        with open('{0}/site.yml'.format(self._project_name), 'w') as writer: writer.write("---")

        ProjectConfig.generate(self._project_name)
        return 0

    def create_role(self, role_name_list: List[str]) -> int:
        """
        Create the role directories and main.yml.
        Return status code.
        That is following to mean:
          0  : success
          3  : validation failed. (Don't exists ansible project file.)
          4  : validation failed. (Don't specify role name.)
        :param role_name_list: role name list.
        :return: status code.
        """
        if not self._is_in_project:
            return 3

        if len(role_name_list) == 0:
            return 4

        for role_name in role_name_list:
            Project.generate_role_files(role_name)

        return 0

    @staticmethod
    def generate_role_files(role_name):
        if not os.path.exists("roles"):
            os.mkdir("roles")
        os.mkdir("roles/{0}".format(role_name))
        os.mkdir("roles/{0}/tasks".format(role_name))
        os.mkdir("roles/{0}/vars".format(role_name))
        os.mkdir("roles/{0}/templates".format(role_name))
        os.mkdir("roles/{0}/files".format(role_name))
        with open('roles/{0}/tasks/main.yml'.format(role_name), 'w') as writer: writer.write("---")
        with open('roles/{0}/vars/main.yml'.format(role_name), 'w') as writer: writer.write("---")
