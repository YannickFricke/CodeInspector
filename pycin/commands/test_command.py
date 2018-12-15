from pycin.commands.Command import Command


class ExampleCommand(Command):
    def __init__(self):
        super().__init__('Test')

    def execute(self, arguments):
        return True


class TestCommand:
    def test_name(self):
        test_command = ExampleCommand()
        assert test_command.name == 'Test'

    def test_execute(self):
        test_command = ExampleCommand()
        assert test_command.execute([])

    def test_str(self):
        command = ExampleCommand()
        assert str(command) == 'Test'
