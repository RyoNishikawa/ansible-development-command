from argparse import ArgumentParser


class CommandParse:

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

