#!/usr/local/bin/python3
import sys
from argparse import ArgumentParser
from project.management import AnsibleProject


class AnsibleDevelopmentCommand:

    _ANSIBLE_VERSION = "0.1.0"

    @classmethod
    def parser(cls):

        parser = ArgumentParser(
            prog='adc',
            description='Ansible Development Command {0}'.format(cls._ANSIBLE_VERSION))

        parser.add_argument(
            'init',
            nargs='*',
            help='Create the directory and few files when specifies this sub command.')

        # subparsers = parser.add_subparsers(help='Sub Commands')
        #
        # parser_init = subparsers.add_parser('init', help='Create the project directory and few files.')
        # parser_init.add_argument(
        #     "init",
        #     action='store_true',
        #     help='Create the directory and few files when specifies this sub command.')

        return parser.parse_args()



def main():
    params = AnsibleDevelopmentCommand.parser()

    if params.__contains__('init'):
        project_name = params.init[1] if len(params.init) >= 2 else ""
        AnsibleProject(project_name).create_project()

    return 0


if __name__ == '__main__':
    sys.exit(main())
