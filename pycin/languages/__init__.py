from abc import ABC, abstractmethod


class Language(ABC):
    def __init__(self, name: str, pretty_name: str):
        """
        Constructs a new 'Language' object
        :param name: The name of the language
        :param pretty_name: The pretty name of the language
        """
        self.name = name
        self.pretty_name = pretty_name

    @abstractmethod
    def get_supported_tools(self):
        """
        Returns an array of supported tools for this language
        :return: The supported tools
        """

    def __str__(self):
        """
        Returns the string representation of the language
        :return: the string representation of the language
        """
        return '{}: {}'.format(self.pretty_name, self.get_supported_tools())
