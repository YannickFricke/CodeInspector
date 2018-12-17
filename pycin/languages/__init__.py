from abc import ABC, abstractmethod
from typing import List

from pycin.package_manager import PackageManager


class Language(ABC):
    def __init__(self,
                 name: str,
                 pretty_name: str,
                 supported_package_managers: List[PackageManager]
                 ):
        """
        Constructs a new 'Language' object
        :param name: The name of the language
        :param pretty_name: The pretty name of the language
        """
        self.name = name
        self.pretty_name = pretty_name
        self.supported_package_managers = supported_package_managers

    @abstractmethod
    def get_supported_tools(self):
        """
        Returns an array of supported supported_tools for this language
        :return: The supported supported_tools
        """

    @abstractmethod
    def setup(self, rootpath: str):
        """
        Sets the language up for saving its configuration to the config file
        :return: A dictionary
        """

    @staticmethod
    @abstractmethod
    def get_pretty_name():
        """
        Returns the pretty name of this code provider
        :return: The pretty name of the code provider
        """

    def get_questions_for_supported_tools(self):
        result = []

        for supported_tool in self.get_supported_tools():
            result.append({
                'type': 'confirm',
                'message': 'Would you like to use {} ({})'.format(
                    supported_tool.pretty_name,
                    supported_tool.name
                ),
                'name': supported_tool.name,
                'default': False,
            })

        return result

    def __str__(self):
        """
        Returns the string representation of the language
        :return: the string representation of the language
        """
        return self.pretty_name
