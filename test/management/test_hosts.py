import unittest

import os
import shutil
import re

# import logging.config
from logging import getLogger
import logging.config


class TestHosts(unittest.TestCase):

    logger = getLogger("test")

    def setUp(self):
        # os.mkdir("tmp")
        # os.chdir("tmp")
        logging.config.fileConfig("../resources/logger.conf")

    def tearDown(self): pass
        # os.chdir("..")
        # shutil.rmtree("tmp")

    def test_add_group(self):
        """
        Add the gourp for hosts.
        """
        test_file_name = "test_hosts_add_group"
        self._create_blank_file(test_file_name)

        InventoryFile(test_file_name).add_group("test_group")

        self.assertTrue(os.path.exists("test_hosts_add_group"))
        with open(test_file_name, 'r') as f:
            result = f.readlines()
            self.logger.debug(result)

        self.assertEqual(result[0], "[test_group]")

    def test_delete_gourp(self):
        """
        Delete the gourp for hosts.
        """

    def test_add_host(self):
        """
        Add the host.
        """
        test_file_name = "test_hosts_add_host"
        self._create_blank_file("test_hosts_add_host")
        #
        InventoryFile(test_file_name).add_host(
            "test_group",
            "test01",
            "192.168.1.10",
            "testuser",
            "testuserpass",
            "testuserpass"
        )

        self.assertTrue(os.path.exists("test_hosts_add_host"))
        with open(test_file_name, 'r') as f:
            result = f.readlines()
            self.logger.debug(result)

        self.assertEqual(result[0], "[test_group]")
        self.assertEqual(
            result[1],
            "test01 "
            "ansible_host=192.168.1.10 "
            "ansible_ssh_user=testuser "
            "ansible_ssh_pass=testuserpass "
            "ansible_sudo_pass=testuserpass"
            "ansible_port=22"
        )


    def test_delete_host(self):
        """
        Delete the host.
        """

    def test_read_hosts(self):
        """
        Read the data in the hosts file.
        """
        test_file_name = "test_hosts_read_hosts"
        self._create_blank_file(test_file_name)
        with open(test_file_name, 'w') as f:
            f.write('\n'.join([
                "[test_group]",
                "test01 "
                "ansible_host=192.168.1.10 "
                "ansible_ssh_user=testuser "
                "ansible_ssh_pass=testuserpass "
                "ansible_sudo_pass=testuserpass "
                "ansible_port=22"
            ]))

        result = InventoryFile(test_file_name)
        result.read_hosts()

        self.assertTrue("test_group" in result.hosts_data)
        self.logger.debug(result.hosts_data['test_group'].hosts[0])
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._host_name, "test01")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_host, "192.168.1.10")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_ssh_user, "testuser")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_ssh_pass, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_sudo_pass, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_port, "22")

    def test_read_hosts_with_two_hosts(self):
        """
        Read the data in the hosts file.
        """
        test_file_name = "test_hosts_read_hosts_with_two_hosts"
        self._create_blank_file(test_file_name)
        with open(test_file_name, 'w') as f:
            f.write('\n'.join([
                "[test_group]",
                "test01 "
                "ansible_host=192.168.1.10 "
                "ansible_ssh_user=testuser "
                "ansible_ssh_pass=testuserpass "
                "ansible_sudo_pass=testuserpass "
                "ansible_port=22",
                "[test_group2]",
                "test02 "
                "ansible_host=192.168.1.11 "
                "ansible_ssh_user=testuser2 "
                "ansible_ssh_pass=testuserpass2 "
                "ansible_sudo_pass=testuserpass2 "
                "ansible_port=23"
            ]))

        result = InventoryFile(test_file_name)
        result.read_hosts()

        self.assertTrue("test_group" in result.hosts_data)
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._host_name, "test01")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_host, "192.168.1.10")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_ssh_user, "testuser")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_ssh_pass, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_sudo_pass, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0]._ansible_port, "22")

        self.assertTrue("test_group2" in result.hosts_data)
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._host_name, "test02")
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._ansible_host, "192.168.1.11")
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._ansible_ssh_user, "testuser2")
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._ansible_ssh_pass, "testuserpass2")
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._ansible_sudo_pass, "testuserpass2")
        # self.assertEqual(result.hosts_data['test_group2'].hosts[0]._ansible_port, "23")

    def _create_blank_file(self, file_name):
        with open(file_name, 'w') as f: pass


class InventoryFile:

    _group_regex = re.compile("\[(.+)\]")

    _inventory_file_name = ""

    _general_group = "general"

    hosts_data = {}

    def __init__(self, inventory_file_name="hosts"):
        self._inventory_file_name = inventory_file_name
        self.hosts_data.update({self._general_group: Group(self._general_group)})

    def add_group(self, group_name):
        with open(self._inventory_file_name, 'w') as f:
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
        with open(self._inventory_file_name, 'w') as f:
            f.write(str(Host(
                host_name,
                ansible_host,
                ansible_ssh_user,
                ansible_ssh_pass,
                ansible_sudo_pass,
                ansible_ssh_port
            )))

    def read_hosts(self):
        group_name = self._general_group
        with open(self._inventory_file_name, 'r') as f:
            for line in f:
                if line is "":
                    group_name = self._general_group
                if self._group_regex.match(line):
                    group_name = self._group_regex.search(line).group(1)
                    self.hosts_data.update({group_name: Group(group_name)})
                else:
                    self.hosts_data[group_name].hosts.append(Host().parse(line))


class Group:
    _group_name = ""

    hosts = []

    def __init__(self, group_name):
        self._group_name = group_name

    def __str__(self):
        result = "[{0}]\n".format(self._group_name)
        return result


class Host:
    _host_name = None

    _ansible_host = None

    _ansible_ssh_user = None

    _ansible_ssh_pass = None

    _ansible_sudo_pass = None

    _ansible_port = None

    _logger = getLogger(__name__)

    def __init__(
            self,
            host_name=None,
            ansible_host=None,
            ansible_ssh_user=None,
            ansible_ssh_pass=None,
            ansible_sudo_pass=None,
            ansible_port=None
    ):
        self._host_name = host_name
        self._ansible_host = ansible_host
        self._ansible_ssh_user = ansible_ssh_user
        self._ansible_ssh_pass = ansible_ssh_pass
        self._ansible_sudo_pass = ansible_sudo_pass
        self._ansible_port = ansible_port

    def __str__(self):
        result = '{0} ' \
                 'ansible_host={1} ' \
                 'ansible_ssh_user={2} ' \
                 'ansible_ssh_pass={3} ' \
                 'ansible_sudo_pass={4} ' \
                 'ansible_port={5}'.format(
                    self._host_name,
                    self._ansible_host,
                    self._ansible_ssh_user,
                    self._ansible_ssh_pass,
                    self._ansible_sudo_pass,
                    self._ansible_port
                )
        return result

    def parse(self, line):
        self._logger.debug("Start parse method.")
        self._logger.debug("---------------------------------------")
        self._logger.debug("args:")
        self._logger.debug("   line = {0}".format(line))
        self._logger.debug("---------------------------------------")
        settings = line.split()
        self._host_name = settings[0]

        for setting in settings[1:]:
            key, value = setting.split("=")

            if key == 'ansible_host':
                self._ansible_host = value
            elif key == 'ansible_ssh_user':
                self._ansible_ssh_user = value
            elif key == 'ansible_ssh_pass':
                self._ansible_ssh_pass = value
            elif key == 'ansible_sudo_pass':
                self._ansible_sudo_pass = value
            elif key == 'ansible_port':
                self._ansible_port = value

        self._logger.debug("End parse method.")
        return self

