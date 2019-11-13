import unittest
import tempfile
import os

from test.util.file import TestFile

from adc.services.management.inventory import Inventory


class TestInventoryService(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_list(self):
        file_name_hosts = 'hosts'
        with tempfile.TemporaryDirectory() as td:
            os.chdir(td)
            TestFile.create_blank_file(file_name_hosts)
            with open(file_name_hosts, 'w') as f:
                for line in ["[test_group]\n",
                             "test01 ansible_host=192.168.1.10 ansible_user=testuser ansible_password=testuserpass ansible_become_password=testuserpass ansible_port=22\n",
                             "[test_group2]\n",
                             "test02 ansible_host=192.168.1.11 ansible_user=testuser2 ansible_password=testuserpass2 ansible_become_password=testuserpass2 ansible_port=23"]:
                    f.write(line)
            test_instance = Inventory()
            test_instance.list()
        pass
