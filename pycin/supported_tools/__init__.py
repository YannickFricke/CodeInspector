from abc import ABC, abstractmethod


class SupportedTool(ABC):
    def __init__(self, name: str, pretty_name: str, executable: str):
        self.name = name
        self.pretty_name = pretty_name
        self.executable = executable
        self.errors = {}

    @abstractmethod
    def execute(self, path: str):
        """
        Executes the supported tool
        :return: True on success. Otherwise false
        """

    def __str__(self):
        return self.pretty_name
