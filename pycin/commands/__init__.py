from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name):
        """
        Initializes the Command
        :param name: The name of the command
        """
        self.name = name

    @abstractmethod
    def execute(self, arguments):
        """
        Executes the command with the given arguments
        :param arguments: The arguments for the execution of the command
        :return: True when the command was executed successfully.
        Otherwise false is returned
        """

    def is_arg_an_option(self, argument: str):
        """
        Returns true when the arguments begins with two dashes
        :param argument: The argument to check
        :return: True when the argument is an option
        """
        return argument.startswith('--')

    def __str__(self):
        """
        Returns the string representation of the command
        :return: The string representation of the command
        """
        return self.name
