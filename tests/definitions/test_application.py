import sys
from unittest import mock

from pycin.definitions.Application import Application


class TestApplication:
    @mock.patch('pycin.commands.Command')
    @mock.patch('logging.Logger')
    def test_run_should_return_false_when_not_enough_arguments_were_given(self, mocked_logger, mocked_command):
        with mock.patch.object(sys, 'argv', ['unit-testing']):
            application = Application(mocked_logger, [mocked_command])
            assert application.run() == False, 'Application#run does not return False when not enough arguments were given'

    @mock.patch('pycin.commands.Command')
    @mock.patch('logging.Logger')
    def test_run_should_execute_the_command(self, mocked_logger, mocked_command):
        mocked_command.configure_mock(name='test')
        with mock.patch.object(sys, 'argv', ['unit-testing', 'test']):
            application = Application(mocked_logger, [mocked_command])
            assert application.run(), 'Application#run does not return True when the command was executed successfully'

    @mock.patch('pycin.commands.Command')
    @mock.patch('logging.Logger')
    def test_run_should_return_false_when_the_command_was_not_found(self, mocked_logger, mocked_command):
        with mock.patch.object(sys, 'argv', ['unit-testing', '']):
            application = Application(mocked_logger, [mocked_command])
            assert application.run() == False, 'Application#run does not return False when the command was not found'
