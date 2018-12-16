import logging
import os

from pycin.commands import Command


class InitCommand(Command):
    def __init__(self, logger: logging.Logger):
        """
        Initializes the InitCommand
        """
        super().__init__('init')
        self.logger = logger

    def execute(self, arguments: []):
        """
        Executes the InitCommand
        :param arguments: The arguments for the execution of the command
        :return: True on success. Otherwise false.
        """
        self.logger.info('Initializing in "%s"!' % os.getcwd())
