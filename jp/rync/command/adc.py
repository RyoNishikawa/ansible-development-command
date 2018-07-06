#!/usr/local/bin/python3
import sys
from argparse import ArgumentParser
from jp.rync.command.project.management import AnsibleProject


class AnsibleDevelopmentCommand:

    _ANSIBLE_VERSION = "0.3.0"

    @classmethod
    def parser(cls):

        parser = ArgumentParser(
            prog='adc',
            description='Ansible Development Command {0}'.format(cls._ANSIBLE_VERSION))

        subparsers = parser.add_subparsers(help='Sub commands')

        parser_init = subparsers.add_parser('init')
        parser_init.add_argument('init_project_name', nargs='?')

        parser_roles = subparsers.add_parser('roles')
        parser_roles.add_argument('-c', '--create', dest='create_role_name')

        return parser.parse_args()



def main():
    params = AnsibleDevelopmentCommand.parser()

    if params.__contains__('init'):
        project_name = params.init[1] if len(params.init) >= 2 else ""
        AnsibleProject(project_name).create_project()

    return 0


if __name__ == '__main__':
    sys.exit(main())
