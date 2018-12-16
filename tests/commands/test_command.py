from pycin.commands import Command


class ExampleCommand(Command):
    def __init__(self):
        super().__init__('Test')

    def execute(self, arguments):
        pass


class TestCommand:
    def test_name(self):
        command = ExampleCommand()
        assert command.name == 'Test'

    def test_is_arg_an_option(self):
        command = ExampleCommand()
        assert command.is_arg_an_option('--arg'), 'A string with two beginning dashes is not an option'
        assert command.is_arg_an_option(
            'arg') == False, 'A string which does not begins with two dashes is not an option'

    def test_str(self):
        command = ExampleCommand()
        assert str(command) == 'Test'
