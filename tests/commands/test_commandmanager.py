from unittest import mock

import pytest

from pycin.definitions.CommandManager import CommandManager


class TestCommandManager:
    @mock.patch('pycin.commands.Command.Command')
    def test_adding_a_command(self, mocked_command):
        command_manager = CommandManager()
        assert len(command_manager.get_commands()) == 0
        command_manager.add_command(mocked_command)
        assert len(command_manager.get_commands()) == 1

    @mock.patch('pycin.commands.Command.Command')
    def test_removing_a_command(self, mocked_command):
        command_manager = CommandManager()
        command_manager.add_command(mocked_command)
        assert len(command_manager.get_commands()) == 1
        command_manager.remove_command(mocked_command)
        assert len(command_manager.get_commands()) == 0

    @mock.patch('pycin.commands.Command.Command')
    def test_execute_a_command_with_the_given_name(self, mocked_command):
        mocked_command.configure_mock(name='Test')
        mocked_command.execute.return_value = True

        command_manager = CommandManager()
        command_manager.add_command(mocked_command)

        assert command_manager.execute('Test', [])

    @mock.patch('pycin.commands.Command.Command')
    def test_should_skip_not_matching_commands(self, mocked_command):
        with pytest.raises(Exception, message=r'.*Test.*'):
            command_manager = CommandManager()
            command_manager.add_command(mocked_command)
            command_manager.execute('test', [])

    def test_throw_an_exception_when_no_command_was_found(self):
        with pytest.raises(Exception, message=r'.*Test.*'):
            command_manager = CommandManager()
            command_manager.execute('test', [])
