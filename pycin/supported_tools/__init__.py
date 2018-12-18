from abc import ABC, abstractmethod
from typing import List

from pycin.package_manager import PackageManager


class SupportedTool(ABC):
    def __init__(self, name: str, pretty_name: str, executable: str):
        self.name = name
        self.pretty_name = pretty_name
        self.executable = executable
        self.errors = {}

    @abstractmethod
    def execute(self,
                path: str,
                package_managers: List[PackageManager]):
        """
        Executes the supported tool
        :return: True on success. Otherwise false
        """

    @staticmethod
    def get_error_dict(message: str,
                       line: int,
                       raw_line: str):
        return {
            'message': message,
            'line': line,
            'raw_line': raw_line
        }

    def __str__(self):
        return self.pretty_name
