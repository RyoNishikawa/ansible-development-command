import unittest

import os

# import logging.config
from logging import getLogger

from adc.models.hosts import InventoryFile


class TestHosts(unittest.TestCase):
    logger = getLogger("test")

    def setUp(self):
        # os.mkdir("tmp")
        # os.chdir("tmp")
        # logging.config.fileConfig("../resources/logger.conf")
        pass

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

        self.assertEqual(result[0], "[test_group]\n")

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
        test_file_name = "test_hosts_read_hosts"
        self._create_blank_file(test_file_name)
        with open(test_file_name, 'w') as f:
            f.write('\n'.join([
                "[test_group]",
                "test01"
                " ansible_host=192.168.1.10"
                " ansible_user=testuser"
                " ansible_password=testuserpass"
                " ansible_become_password=testuserpass"
                " ansible_port=22"
            ]))

        result = InventoryFile(test_file_name)
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
        test_file_name = "test_hosts_read_hosts_with_two_hosts"
        self._create_blank_file(test_file_name)
        with open(test_file_name, 'w') as f:
            for line in ["[test_group]\n",
                         "test01 ansible_host=192.168.1.10 ansible_user=testuser ansible_password=testuserpass ansible_become_password=testuserpass ansible_port=22\n",
                         "[test_group2]\n",
                         "test02 ansible_host=192.168.1.11 ansible_user=testuser2 ansible_password=testuserpass2 ansible_become_password=testuserpass2 ansible_port=23"]:
                f.write(line)
            # f.writelines([
            #     "[test_group]\n",
            #     "test01 ansible_host=192.168.1.10 ansible_user=testuser ansible_password=testuserpass ansible_become_password=testuserpass ansible_port=22\n",
            #     "[test_group2]\n",
            #     "test02 ansible_host=192.168.1.11 ansible_user=testuser2 ansible_password=testuserpass2 ansible_become_password=testuserpass2 ansible_port=23"
            # ])
            # f.write('\n'.join([
            #     "[test_group]",
            #     "test01"
            #     " ansible_host=192.168.1.10"
            #     " ansible_user=testuser"
            #     " ansible_password=testuserpass"
            #     " ansible_become_password=testuserpass"
            #     " ansible_port=22",
            #     "[test_group2]",
            #     "test02"
            #     " ansible_host=192.168.1.11"
            #     " ansible_user=testuser2"
            #     " ansible_password=testuserpass2"
            #     " ansible_become_password=testuserpass2"
            #     " ansible_port=23"
            # ]))

        result = InventoryFile(test_file_name)
        result.read_hosts()

        # print(result.hosts_data)
        # print("========= result ==========")
        # for line in result.hosts_data['test_group'].hosts:
        #     print(line)
        # print("========= result2 =========")
        # for line in result.hosts_data['test_group2'].hosts:
        #     print(line)
        # print("===========================")

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

    def _create_blank_file(self, file_name):
        with open(file_name, 'w') as f: pass

