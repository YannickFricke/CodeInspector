from pycin.commands import Command


class ExampleCommand(Command):
    def __init__(self):
        super().__init__('Test')

    def execute(self, arguments):
        pass


class TestCommand:
    def test_name(self):
        test_command = ExampleCommand()
        assert test_command.name == 'Test'

    def test_str(self):
        command = ExampleCommand()
        assert str(command) == 'Test'
