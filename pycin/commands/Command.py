from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, arguments):
        """
        Executes the command with the given arguments
        :param arguments: The arguments for the command
        :return: True when the command was executed successfully.
        Otherwise false is returned
        """

    def __str__(self):
        return self.name
