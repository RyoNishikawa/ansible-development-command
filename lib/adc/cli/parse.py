from argparse import ArgumentParser, _SubParsersAction


class CommandParse:

    _ANSIBLE_VERSION = "0.3.0"

    @classmethod
    def parser(cls):

        parser: ArgumentParser = ArgumentParser(
            prog='adc',
            description='Ansible Development Command {0}'.format(cls._ANSIBLE_VERSION))

        subparsers: _SubParsersAction = parser.add_subparsers(help='Sub commands')
        ####################################################################################################
        # init sub command
        parser_init: ArgumentParser = subparsers.add_parser('init')
        parser_init.add_argument('init_project_name', nargs='?')

        ####################################################################################################
        # list sub command
        parser_list: ArgumentParser = subparsers.add_parser('list')
        parser_list_subparsers: _SubParsersAction = parser_list.add_subparsers(help='List sub commands')

        # list hosts
        parser_list_hosts: ArgumentParser = parser_list_subparsers.add_parser('hosts')
        parser_list_hosts.add_argument('list_hosts', action='store_true')

        ####################################################################################################
        # create sub command
        parser_create: ArgumentParser = subparsers.add_parser('create')
        parser_create_subparsers: _SubParsersAction = parser_create.add_subparsers(help='Create sub commands')

        # create roles
        parser_create_roles: ArgumentParser = parser_create_subparsers.add_parser('roles')
        parser_create_roles.add_argument('create_role_name', nargs='+')

        return parser.parse_args()

