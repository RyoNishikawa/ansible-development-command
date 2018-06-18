import unittest

import os
import shutil

import configparser

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
            print(f.readline())

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

    def __init__(self, group_name):
        self._group_name = group_name


class Host:
    _host_name = ""

    def __init__(self, host_name):
        self._host_name = host_name
