import unittest

import os
import shutil

from jp.rync.command.project.management import AnsibleProject

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
        self._create_blank_file("test_hosts_add_group")

        Hosts().add_group("test_group")

        self.assertTrue(os.path.exists("test_hosts_add_group"))

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


class Hosts:

    _project = None

    def __init__(self): pass

    def add_group(self, group_name):
        with open("hosts", 'w') as f:
            f.write("[{0}]".format(group_name))
