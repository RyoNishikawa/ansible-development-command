import unittest

import os
import shutil


class TestHosts(unittest.TestCase):

    def setUp(self):
        os.mkdir("tmp")
        os.chdir("tmp")

    def tearDown(self):
        os.chdir("..")
        shutil.rmtree("tmp")

    def test_add_group(self):
        """
        Add the gourp for hosts.
        """
        test_file_name = "test_hosts_add_group"
        self._create_blank_file("test_hosts_add_group")

        InventoryFile(test_file_name).add_group("test_group")

        self.assertTrue(os.path.exists("test_hosts_add_group"))
        with open(test_file_name, 'r') as f:
            result = f.readlines()
            print(result)

        self.assertEqual(result[0], "[test_group]")

    def test_delete_gourp(self):
        """
        Delete the gourp for hosts.
        """

    def test_add_host(self):
        """
        Add the host.
        """

    def test_delete_host(self):
        """
        Delete the host.
        """

    def test_read_hosts(self):
        """
        Read the data in the hosts file.
        """

    def _create_blank_file(self, file_name):
        with open(file_name, 'w') as f: pass


class InventoryFile:

    _inventory_file_name = ""

    def __init__(self, inventory_file_name="hosts"):
        self._inventory_file_name = inventory_file_name

    def add_group(self, group_name):
        with open(self._inventory_file_name, 'w') as f:
            f.write("[{0}]".format(group_name))


class Group:
    _group_name = ""

    _hosts = {}

    def __init__(self, group_name):
        self._group_name = group_name

    def to_string(self):
        return "[{0}]".format(self._group_name)


class Host:
    _host_name = None

    _ansible_host = None

    _ansible_ssh_user = None

    _ansible_ssh_pass = None

    _ansible_sudo_pass = None

    _ansible_port = None

    def __init__(
            self,
            host_name,
            ansible_host,
            ansible_ssh_user,
            ansible_ssh_pass,
            ansible_sudo_pass,
            ansible_port=22,
    ):
        self._host_name = host_name
        self._ansible_host = ansible_host
        self._ansible_ssh_user = ansible_ssh_user
        self._ansible_ssh_pass = ansible_ssh_pass
        self._ansible_sudo_pass = ansible_sudo_pass
        self._ansible_port = ansible_port

    def to_string(self):
        result = '{0} ' \
                 'ansible_host="{1}" ' \
                 'ansible_ssh_user="{2}" ' \
                 'ansible_ssh_pass="{3}" ' \
                 'ansible_sudo_pass="{4}" ' \
                 'ansible_port="{5}"'.format(
                    self._host_name,
                    self._ansible_host,
                    self._ansible_ssh_user,
                    self._ansible_ssh_pass,
                    self._ansible_sudo_pass,
                    self._ansible_port
                )
