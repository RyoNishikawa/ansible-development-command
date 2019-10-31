import re
from typing import List, Dict


class Interpreter:
    type_str: str
    value: str

    def __init__(self, type_str: str, value: str):
        self.type_str = type_str
        self.value = value

    def __str__(self):
        return "ansible_{0}_interpreter={1}".format(self.type_str, self.value)


class Host:
    regex_host_name = re.compile(r'^([^ ]*) .*')
    regex_ansible_connection = re.compile(r'.*ansible_connection *= *([^ ]*).*')
    regex_ansible_host = re.compile(r'.*ansible_host *= *([^ ]*).*')
    regex_ansible_port = re.compile(r'.*ansible_port *= *([^ ]*).*')
    regex_ansible_user = re.compile(r'.*ansible_user *= *([^ ]*).*')
    regex_ansible_password = re.compile(r'.*ansible_password *= *([^ ]*).*')
    regex_ansible_ssh_private_key_file = re.compile(r'.*ansible_ssh_private_key_file *= *([^ ]*).*')
    regex_ansible_ssh_common_args = re.compile(r'.*ansible_ssh_common_args *= *([^ ]*).*')
    regex_ansible_sftp_extra_args = re.compile(r'.*ansible_sftp_extra_args *= *([^ ]*).*')
    regex_ansible_scp_extra_args = re.compile(r'.*ansible_scp_extra_args *= *([^ ]*).*')
    regex_ansible_ssh_extra_args = re.compile(r'.*ansible_ssh_extra_args *= *([^ ]*).*')
    regex_ansible_ssh_pipelining = re.compile(r'.*ansible_ssh_pipelining *= *([^ ]*).*')
    regex_ansible_ssh_executable = re.compile(r'.*ansible_ssh_executable *= *([^ ]*).*')
    regex_ansible_become = re.compile(r'.*ansible_become *= *([^ ]*).*')
    regex_ansible_become_method = re.compile(r'.*ansible_become_method *= *([^ ]*).*')
    regex_ansible_become_user = re.compile(r'.*ansible_become_user *= *([^ ]*).*')
    regex_ansible_become_password = re.compile(r'.*ansible_become_password *= *([^ ]*).*')
    regex_ansible_become_exe = re.compile(r'.*ansible_become_exe *= *([^ ]*).*')
    regex_ansible_become_flags = re.compile(r'.*ansible_become_flags *= *([^ ]*).*')
    regex_ansible_shell_type = re.compile(r'.*ansible_shell_type *= *([^ ]*).*')
    regex_ansible_python_interpreter = re.compile(r'.*ansible_python_interpreter *= *([^ ]*).*')
    regex_ansible_interpreter = re.compile(r'.*ansible_([a-zA-Z]+)_interpreter *= *([^ ]*).*')
    regex_ansible_shell_executable = re.compile(r'.*ansible_shell_executable *= *([^ ]*).*')

    host_name: str
    option_ansible_connection: str
    option_ansible_host: str
    option_ansible_port: str
    option_ansible_user: str
    option_ansible_password: str
    option_ansible_ssh_private_key_file: str
    option_ansible_ssh_common_args: str
    option_ansible_sftp_extra_args: str
    option_ansible_scp_extra_args: str
    option_ansible_ssh_extra_args: str
    option_ansible_ssh_pipelining: str
    option_ansible_ssh_executable: str  # added in version 2.2
    option_ansible_become: str
    option_ansible_become_method: str
    option_ansible_become_user: str
    option_ansible_become_password: str
    option_ansible_become_exe: str
    option_ansible_become_flags: str
    option_ansible_shell_type: str
    option_list_ansible_python_interpreter: List[Interpreter]
    option_ansible_interpreter: str
    option_ansible_shell_executable: str

    def __init__(self,
                 host_name: str,
                 ansible_connection: str = 'ssh',
                 ansible_host: str = None,
                 ansible_port: str = None,
                 ansible_user: str = None,
                 ansible_password: str = None,
                 ansible_ssh_private_key_file: str = None,
                 ansible_ssh_common_args: str = None,
                 ansible_sftp_extra_args: str = None,
                 ansible_scp_extra_args: str = None,
                 ansible_ssh_extra_args: str = None,
                 ansible_ssh_pipelining: str = None,
                 ansible_ssh_executable: str = None,  # added in version 2.2
                 ansible_become: str = None,
                 ansible_become_method: str = None,
                 ansible_become_user: str = None,
                 ansible_become_password: str = None,
                 ansible_become_exe: str = None,
                 ansible_become_flags: str = None,
                 ansible_shell_type: str = None,
                 ansible_python_interpreter: str = None,
                 ansible_interpreter: List[Interpreter] = None,
                 ansible_shell_executable: str = None
                 ):
        self.host_name = host_name
        self.option_ansible_connection = ansible_connection
        self.option_ansible_host = ansible_host
        self.option_ansible_port = ansible_port
        self.option_ansible_user = ansible_user
        self.option_ansible_password = ansible_password
        self.option_ansible_ssh_private_key_file = ansible_ssh_private_key_file
        self.option_ansible_ssh_common_args = ansible_ssh_common_args
        self.option_ansible_sftp_extra_args = ansible_sftp_extra_args
        self.option_ansible_scp_extra_args = ansible_scp_extra_args
        self.option_ansible_ssh_extra_args = ansible_ssh_extra_args
        self.option_ansible_ssh_pipelining = ansible_ssh_pipelining
        self.option_ansible_ssh_executable = ansible_ssh_executable
        self.option_ansible_become = ansible_become
        self.option_ansible_become_method = ansible_become_method
        self.option_ansible_become_user = ansible_become_user
        self.option_ansible_become_password = ansible_become_password
        self.option_ansible_become_exe = ansible_become_exe
        self.option_ansible_become_flags = ansible_become_flags
        self.option_ansible_shell_type = ansible_shell_type
        # self.list_ansible_python_interpreter = ansible_python_interpreter
        # self.ansible_interpreter = ansible_interpreter
        self.option_ansible_shell_executable = ansible_shell_executable

    def __str__(self):
        space: str = ' '
        result: str = self.host_name
        for (symbol, value) in self.__dict__.items():
            if symbol.startswith('option_') and value is not None:
                result += "{0}{1}={2}".format(space, symbol.replace('option_', ''), value)
        result += '\n'
        return result

    @classmethod
    def parser(cls, line: str):
        target = line.replace('\n', '')
        methods = cls.__dict__.items()
        for (symbol, value) in methods:
            if symbol.startswith('regex_'):
                result = value.match(target)
                if result is not None:
                    locals()[str(symbol.replace('regex_', ''))] = result.group(1)
                else:
                    locals()[str(symbol.replace('regex_', ''))] = result

        return Host(host_name=locals()['host_name'],
                    ansible_connection='ssh' if locals()['ansible_connection'] is None else locals()['ansible_connection'],
                    ansible_host=locals()['ansible_host'],
                    ansible_port=locals()['ansible_port'],
                    ansible_user=locals()['ansible_user'],
                    ansible_password=locals()['ansible_password'],
                    ansible_ssh_private_key_file=locals()['ansible_ssh_private_key_file'],
                    ansible_ssh_common_args=locals()['ansible_ssh_common_args'],
                    ansible_sftp_extra_args=locals()['ansible_sftp_extra_args'],
                    ansible_scp_extra_args=locals()['ansible_scp_extra_args'],
                    ansible_ssh_extra_args=locals()['ansible_ssh_extra_args'],
                    ansible_ssh_pipelining=locals()['ansible_ssh_pipelining'],
                    ansible_ssh_executable=locals()['ansible_ssh_executable'],
                    ansible_become=locals()['ansible_become'],
                    ansible_become_method=locals()['ansible_become_method'],
                    ansible_become_user=locals()['ansible_become_user'],
                    ansible_become_password=locals()['ansible_become_password'],
                    ansible_become_exe=locals()['ansible_become_exe'],
                    ansible_become_flags=locals()['ansible_become_flags'],
                    ansible_shell_type=locals()['ansible_shell_type'],
                    # ansible_python_interpreter=locals()['ansible_python_interpreter'],
                    # ansible_interpreter: List[Interpreter]=locals()['ansible_interpreter'],
                    ansible_shell_executable=locals()['ansible_shell_executable'])


class Group:
    _group_name = ""

    hosts: List[Host]

    def __init__(self, group_name):
        self._group_name = group_name
        self.hosts = []

    def __str__(self):
        result = "[{0}]\n".format(self._group_name)
        return result

    def append_host(self, host: Host):
        self.hosts.append(host)


class InventoryFile:
    _group_regex = re.compile("\[(.+)\]")

    _inventory_file_name: str

    _general_group: str = "general"

    hosts_data: Dict[str, Group]

    def __init__(self, inventory_file_name="hosts"):
        self._inventory_file_name = inventory_file_name
        self.hosts_data = {self._general_group: Group(self._general_group)}

    def add_group(self, group_name):
        with open(self._inventory_file_name, 'a') as f:
            f.write(str(Group(group_name)))

    def add_host(
            self,
            group_name,
            host_name,
            ansible_host,
            ansible_ssh_user,
            ansible_ssh_pass,
            ansible_sudo_pass,
            ansible_ssh_port="22"
    ):
        self.add_group(group_name)
        with open(self._inventory_file_name, 'a') as f:
            f.write(str(Host(
                host_name=host_name,
                ansible_host=ansible_host,
                ansible_user=ansible_ssh_user,
                ansible_password=ansible_ssh_pass,
                ansible_become_password=ansible_sudo_pass,
                ansible_port=ansible_ssh_port
            )))

    def append_group(self, group_name: str):
        group = Group(group_name)
        self.hosts_data.update({group_name: group})

    def read_hosts(self):
        group_name = self._general_group
        with open(self._inventory_file_name, 'r') as f:
            for line in f:
                if line is "":
                    group_name = self._general_group
                elif self._group_regex.match(line):
                    group_name = self._group_regex.search(line).group(1)
                    self.append_group(group_name)
                else:
                    self.hosts_data[group_name].append_host(Host.parser(line))