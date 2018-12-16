from pycin.commands import Command


class CommandManager:
    def __init__(self):
        """
        Initializes the CommandManager
        """
        self.commands = []

    def add_command(self, command: Command):
        """
        Adds a Command to the CommandManager
        :param command: The command to add
        """
        self.commands.append(command)

    def remove_command(self, command: Command):
        """
        Removes a Command from the CommandManager
        :param command: The Command to remove
        """
        self.commands.remove(command)

    def execute(self, command_name: str, command_args: []):
        """
        Executes a Command with the given name and the given arguments
        :param command_name: The name of the Command to execute
        :param command_args: The arguments for the Command
        :return:
        """
        for command in self.commands:
            if command.name != command_name:
                continue

            return command.execute(command_args)

        raise Exception(
            'No command with the name "{}" found'.format(command_name)
        )

    def get_commands(self):
        """
        Returns all registered commands
        :return: All registered commands
        """
        return self.commands
