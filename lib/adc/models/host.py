import re


class Host:

    host_name_regex = re.compile(r'^([^ ]*) .*')
    ansible_connection_regex = re.compile(r'.*ansible_connection *= *([^ ]*).*')
    ansible_host_regex = re.compile(r'.*ansible_host *= *([^ ]*).*')
    ansible_port_regex = re.compile(r'.*ansible_port *= *([^ ]*).*')
    ansible_user_regex = re.compile(r'.*ansible_user *= *([^ ]*).*')
    ansible_password_regex = re.compile(r'.*ansible_password *= *([^ ]*).*')
    ansible_ssh_private_key_file_regex = re.compile(r'.*ansible_ssh_private_key_file *= *([^ ]*).*')
    ansible_ssh_common_args_regex = re.compile(r'.*ansible_ssh_common_args *= *([^ ]*).*')
    ansible_sftp_extra_args_regex = re.compile(r'.*ansible_sftp_extra_args *= *([^ ]*).*')
    ansible_scp_extra_args_regex = re.compile(r'.*ansible_scp_extra_args *= *([^ ]*).*')
    ansible_ssh_extra_args_regex = re.compile(r'.*ansible_ssh_extra_args *= *([^ ]*).*')
    ansible_ssh_pipelining_regex = re.compile(r'.*ansible_ssh_pipelining *= *([^ ]*).*')
    ansible_ssh_executable_regex = re.compile(r'.*ansible_ssh_executable *= *([^ ]*).*')
    ansible_become_regex = re.compile(r'.*ansible_become *= *([^ ]*).*')
    ansible_become_method_regex = re.compile(r'.*ansible_become_method *= *([^ ]*).*')
    ansible_become_user_regex = re.compile(r'.*ansible_become_user *= *([^ ]*).*')
    ansible_become_password_regex = re.compile(r'.*ansible_become_password *= *([^ ]*).*')
    ansible_become_exe_regex = re.compile(r'.*ansible_become_exe *= *([^ ]*).*')
    ansible_become_flags_regex = re.compile(r'.*ansible_become_flags *= *([^ ]*).*')
    ansible_shell_type_regex = re.compile(r'.*ansible_shell_type *= *([^ ]*).*')
    ansible_python_interpreter_regex = re.compile(r'.*ansible_python_interpreter *= *([^ ]*).*')
    ansible_interpreter_regex = re.compile(r'.*ansible_([a-zA-Z]+)_interpreter *= *([^ ]*).*')
    ansible_shell_executable_regex = re.compile(r'.*ansible_shell_executable *= *([^ ]*).*')

    host_name: str
    ansible_connection: str
    ansible_host: str
    ansible_port: str
    ansible_user: str
    ansible_password: str
    ansible_ssh_private_key_file: str
    ansible_ssh_common_args: str
    ansible_sftp_extra_args: str
    ansible_scp_extra_args: str
    ansible_ssh_extra_args: str
    ansible_ssh_pipelining: str
    ansible_ssh_executable: str              #added in version 2.2
    ansible_become: str
    ansible_become_method: str
    ansible_become_user: str
    ansible_become_password: str
    ansible_become_exe: str
    ansible_become_flags: str
    ansible_shell_type: str
    ansible_python_interpreter: str
    ansible_interpreter: str
    ansible_shell_executable: str

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
                 ansible_ssh_executable: str = None,              #added in version 2.2
                 ansible_become: str = None,
                 ansible_become_method: str = None,
                 ansible_become_user: str = None,
                 ansible_become_password: str = None,
                 ansible_become_exe: str = None,
                 ansible_become_flags: str = None,
                 ansible_shell_type: str = None,
                 ansible_python_interpreter: str = None,
                 ansible_interpreter: str = None,
                 ansible_shell_executable: str = None
                 ):
        self.host_name = host_name
        self.ansible_connection = ansible_connection
        self.ansible_host = ansible_host
        self.ansible_port = ansible_port
        self.ansible_user = ansible_user
        self.ansible_password = ansible_password
        self.ansible_ssh_private_key_file = ansible_ssh_private_key_file
        self.ansible_ssh_common_args = ansible_ssh_common_args
        self.ansible_sftp_extra_args = ansible_sftp_extra_args
        self.ansible_scp_extra_args = ansible_scp_extra_args
        self.ansible_ssh_extra_args = ansible_ssh_extra_args
        self.ansible_ssh_pipelining = ansible_ssh_pipelining
        self.ansible_ssh_executable = ansible_ssh_executable
        self.ansible_become = ansible_become
        self.ansible_become_method = ansible_become_method
        self.ansible_become_user = ansible_become_user
        self.ansible_become_password = ansible_become_password
        self.ansible_become_exe = ansible_become_exe
        self.ansible_become_flags = ansible_become_flags
        self.ansible_shell_type = ansible_shell_type
        self.ansible_python_interpreter = ansible_python_interpreter
        self.ansible_interpreter = ansible_interpreter
        self.ansible_shell_executable = ansible_shell_executable

    def __str__(self):
        space: str = ' '
        result: str = self.host_name

        result = "" if self.ansible_host is None else result + space + self.ansible_host
        result = "" if self.ansible_port is None else result + space + self.ansible_port
        result = "" if self.ansible_user is None else result + space + self.ansible_user
        result = "" if self.ansible_password is None else result + space + self.ansible_password
        result = "" if self.ansible_ssh_private_key_file is None else result + space + self.ansible_ssh_private_key_file
        result = "" if self.ansible_ssh_common_args is None else result + space + self.ansible_ssh_common_args
        result = "" if self.ansible_sftp_extra_args is None else result + space + self.ansible_sftp_extra_args
        result = "" if self.ansible_scp_extra_args is None else result + space + self.ansible_scp_extra_args
        result = "" if self.ansible_ssh_extra_args is None else result + space + self.ansible_ssh_extra_args
        result = "" if self.ansible_ssh_pipelining is None else result + space + self.ansible_ssh_pipelining
        result = "" if self.ansible_ssh_executable is None else result + space + self.ansible_ssh_executable
        result = "" if self.ansible_become is None else result + space + self.ansible_become
        result = "" if self.ansible_become_method is None else result + space + self.ansible_become_method
        result = "" if self.ansible_become_user is None else result + space + self.ansible_become_user
        result = "" if self.ansible_become_password is None else result + space + self.ansible_become_password
        result = "" if self.ansible_become_exe is None else result + space + self.ansible_become_exe
        result = "" if self.ansible_become_flags is None else result + space + self.ansible_become_flags
        result = "" if self.ansible_shell_type is None else result + space + self.ansible_shell_type
        result = "" if self.ansible_python_interpreter is None else result + space + self.ansible_python_interpreter
        result = "" if self.ansible_interpreter is None else result + space + self.ansible_interpreter
        result = "" if self.ansible_shell_executable is None else result + space + self.ansible_shell_executable

        return result

    @staticmethod
    def parser(line: str):
        pass


class Interpreter:
    type_str: str
    value: str

    def __init__(self, type_str: str, value: str):
        self.type_str = type_str
        self.value = value

    def __str__(self):
        return "ansible_{0}_interpreter={1}".format(self.type_str, self.value)
