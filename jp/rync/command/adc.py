#!/usr/local/bin/python3
import sys
from argparse import ArgumentParser


class AnsibleDevelopmentCommand:

    _ANSIBLE_VERSION = "0.1.0"

    @classmethod
    def parser(cls, args):

        if sys.argv:
            del args[0:]

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

        print(args)
        return parser.parse_args(args)



def main(args=sys.argv):
    print(args)
    params = AnsibleDevelopmentCommand.parser(args)
    print(params)
    return 0


if __name__ == '__main__':
    sys.exit(main())
