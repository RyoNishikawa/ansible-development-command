import os
import shutil

from typing import List


class TestFile:

    @staticmethod
    def create_blank_file(file_name: str):
        if not os.path.exists(file_name):
            with open(file_name, 'w') as f: pass

    @staticmethod
    def create_blank_directory(directory_name: str):
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)

    @staticmethod
    def delete_file(file_name: str):
        if os.path.exists(file_name):
            os.remove(file_name)

    @staticmethod
    def delete_files(file_names: List[str]):
        for file_name in file_names:
            TestFile.delete_file(file_name)

    @staticmethod
    def delete_directory(directory_name: str):
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)

    @staticmethod
    def delete_directories(directory_names: List[str]):
        for directory_name in directory_names:
            TestFile.delete_directory(directory_name)
