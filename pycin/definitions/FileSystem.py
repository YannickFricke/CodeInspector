import os
from typing import List

from pycin.package_manager import PackageManager

ignored_directories = [
    '.git',
    '.idea',
    '__pycache__'
]

CONFIG_FILE_NAME = '.pycin.yaml'


class FileSystem:
    @staticmethod
    def get_directories(path: str):
        """
        Returns all directories for the given path
        :param path: The path where to check for the directories
        :return: The directories in the path
        """
        path = FileSystem().ensure_trailing_path_seperator(path)
        return list(filter(lambda item: os.path.isdir(path + item), os.listdir(path)))

    @staticmethod
    def get_filtered_directories(rootpath: str):
        """
        Returns a list of directories
        :param rootpath:
        :return:
        """
        return list(
            filter(
                lambda item: item not in ignored_directories,
                FileSystem.get_directories(rootpath)
            )
        )

    @staticmethod
    def get_binary_path(
            binary_name: str,
            package_managers: List[PackageManager]
    ):
        for package_manager in package_managers:
            path_to_check = FileSystem.compute_path(
                package_manager.binary_directory,
                binary_name
            )
            if os.path.isfile(path_to_check):
                return path_to_check

            path_to_check = FileSystem.compute_path(
                package_manager.global_binary_directory,
                binary_name
            )
            if os.path.isfile(path_to_check):
                return path_to_check

            for path_part in os.get_exec_path():
                path_to_check = FileSystem.compute_path(
                    path_part,
                    binary_name
                )
                if os.path.isfile(path_to_check):
                    return path_to_check

        return None

    @staticmethod
    def compute_path(binary_directory: str, executable_name: str):
        return '{}{}'.format(
            FileSystem().ensure_trailing_path_seperator(binary_directory),
            executable_name
        )

    @staticmethod
    def ensure_trailing_path_seperator(path_to_check: str):
        if path_to_check.endswith(os.sep):
            return path_to_check

        return path_to_check + os.sep
