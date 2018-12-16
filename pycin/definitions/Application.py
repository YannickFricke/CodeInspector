import logging
import sys

from pycin.definitions.CommandManager import CommandManager


class Application:
    def __init__(self, logger: logging.Logger, known_commands: []):
        self.logger = logger
        self.known_commands = known_commands

    def run(self):
        command_manager = CommandManager()

        for command in self.known_commands:
            command_manager.add_command(command)

        program_arguments = sys.argv[1:]

        command = program_arguments[0]
        program_arguments = program_arguments[1:]

        try:
            command_manager.execute(command, program_arguments)
        except Exception as exception:
            self.logger.error(
                'Could not start application: %s',
                str(exception)
            )
            self.display_help()
            sys.exit(1)

    @staticmethod
    def display_help():
        print()
        print('PyCIn (Code Inspector)')
