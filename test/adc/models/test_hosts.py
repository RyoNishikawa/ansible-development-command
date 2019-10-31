import unittest

import os

# import logging.config
from logging import getLogger

from adc.models.inventory import InventoryFile


class TestHosts(unittest.TestCase):
    logger = getLogger("test")

    file_name_test_hosts_add_group = "test_hosts_add_group"
    file_name_test_hosts_add_host = "test_hosts_add_host"
    file_name_test_hosts_read_hosts = "test_hosts_read_hosts"
    file_name_test_hosts_read_hosts_with_two_hosts = "test_hosts_read_hosts_with_two_hosts"

    def setUp(self):
        # logging.config.fileConfig("../resources/logger.conf")
        self.delete_test_files()
        pass

    def tearDown(self):
        self.delete_test_files()
        pass

    def delete_test_files(self):
        files = [
            self.file_name_test_hosts_add_group,
            self.file_name_test_hosts_add_host,
            self.file_name_test_hosts_read_hosts,
            self.file_name_test_hosts_read_hosts_with_two_hosts
        ]
        for file_name in files:
            self._delete_file(file_name)

    # os.chdir("..")
    # shutil.rmtree("tmp")

    def test_add_group(self):
        """
        Add the gourp for hosts.
        """
        self._create_blank_file(self.file_name_test_hosts_add_group)

        InventoryFile(self.file_name_test_hosts_add_group).add_group("test_group")

        self.assertTrue(os.path.exists(self.file_name_test_hosts_add_group))
        with open(self.file_name_test_hosts_add_group, 'r') as f:
            result = f.readlines()
            self.logger.debug(result)

        self.assertEqual(result[0], "[test_group]\n")

    def test_delete_gourp(self):
        """
        Delete the gourp for hosts.
        """

    def test_add_host(self):
        """
        Add the host.
        """
        self._create_blank_file(self.file_name_test_hosts_add_host)
        #
        InventoryFile(self.file_name_test_hosts_add_host).add_host(
            "test_group",
            "test01",
            "192.168.1.10",
            "testuser",
            "testuserpass",
            "testuserpass"
        )

        self.assertTrue(os.path.exists(self.file_name_test_hosts_add_host))
        with open(self.file_name_test_hosts_add_host, 'r') as f:
            result = f.readlines()
            self.logger.debug(result)

        self.assertEqual(result[0], "[test_group]\n")
        self.assertEqual(
            result[1],
            "test01"
            " ansible_connection=ssh"
            " ansible_host=192.168.1.10"
            " ansible_port=22"
            " ansible_user=testuser"
            " ansible_password=testuserpass"
            " ansible_become_password=testuserpass\n"
        )

    def test_delete_host(self):
        """
        Delete the host.
        """

    def test_read_hosts(self):
        """
        Read the data in the hosts file.
        """
        self._create_blank_file(self.file_name_test_hosts_read_hosts)
        with open(self.file_name_test_hosts_read_hosts, 'w') as f:
            f.write('\n'.join([
                "[test_group]",
                "test01"
                " ansible_host=192.168.1.10"
                " ansible_user=testuser"
                " ansible_password=testuserpass"
                " ansible_become_password=testuserpass"
                " ansible_port=22"
            ]))

        result = InventoryFile(self.file_name_test_hosts_read_hosts)
        result.read_hosts()

        self.assertTrue("test_group" in result.hosts_data)
        self.assertEqual(result.hosts_data['test_group'].hosts[0].host_name, "test01")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_host, "192.168.1.10")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_user, "testuser")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_password, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_become_password, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_port, "22")

    def test_read_hosts_with_two_hosts(self):
        """
        Read the data in the hosts file.
        """
        self._create_blank_file(self.file_name_test_hosts_read_hosts_with_two_hosts)
        with open(self.file_name_test_hosts_read_hosts_with_two_hosts, 'w') as f:
            for line in ["[test_group]\n",
                         "test01 ansible_host=192.168.1.10 ansible_user=testuser ansible_password=testuserpass ansible_become_password=testuserpass ansible_port=22\n",
                         "[test_group2]\n",
                         "test02 ansible_host=192.168.1.11 ansible_user=testuser2 ansible_password=testuserpass2 ansible_become_password=testuserpass2 ansible_port=23"]:
                f.write(line)

        result = InventoryFile(self.file_name_test_hosts_read_hosts_with_two_hosts)
        result.read_hosts()

        self.assertTrue("test_group" in result.hosts_data)
        self.assertEqual(result.hosts_data['test_group'].hosts[0].host_name, "test01")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_host, "192.168.1.10")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_user, "testuser")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_password, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_become_password, "testuserpass")
        self.assertEqual(result.hosts_data['test_group'].hosts[0].option_ansible_port, "22")

        self.assertTrue("test_group2" in result.hosts_data)
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].host_name, "test02")
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].option_ansible_host, "192.168.1.11")
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].option_ansible_user, "testuser2")
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].option_ansible_password, "testuserpass2")
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].option_ansible_become_password, "testuserpass2")
        self.assertEqual(result.hosts_data['test_group2'].hosts[0].option_ansible_port, "23")

    def _create_blank_file(self, file_name: str):
        with open(file_name, 'w') as f: pass

    def _delete_file(self, file_name: str):
        if os.path.exists(file_name):
            os.remove(file_name)
