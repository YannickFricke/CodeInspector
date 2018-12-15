class CommandManager:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def remove_command(self, command):
        self.commands.remove(command)

    def execute(self, command_name, command_args):
        for command in self.commands:
            if command.name != command_name:
                continue

            return command.execute(command_args)

        raise Exception(
            'No command with the name "{}" found'.format(command_name)
        )

    def get_commands(self):
        return self.commands
