import logging
import os
from typing import List

from pycin.commands import Command
from pycin.languages import Language


class InitCommand(Command):
    def __init__(self,
                 logger: logging.Logger,
                 supported_languages: List[Language]):
        """
        Initializes the InitCommand
        """
        super().__init__('init')
        self.logger = logger

    def execute(self, arguments: List[str]):
        """
        Executes the InitCommand
        :param arguments: The arguments for the execution of the command
        :return: True on success. Otherwise false.
        """
        self.logger.info('Initializing in "%s"!' % os.getcwd())
        return True
