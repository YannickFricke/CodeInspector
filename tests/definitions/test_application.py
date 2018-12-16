import sys
from unittest import mock

import pytest

from pycin.definitions.Application import Application


class TestApplication:
    @mock.patch('pycin.commands.Command')
    @mock.patch('logging.Logger')
    def test_run_should_execute_the_command(self, mocked_logger, mocked_command):
        mocked_command.configure_mock(name='test')
        with mock.patch.object(sys, 'argv', ['unit-testing', 'test']):
            application = Application(mocked_logger, [mocked_command])
            application.run()

    @mock.patch('pycin.commands.Command')
    @mock.patch('logging.Logger')
    def test_run_should_exit_when_the_command_was_not_found(self, mocked_logger, mocked_command):
        with mock.patch.object(sys, 'argv', ['unit-testing', '']):
            with pytest.raises(SystemExit):
                application = Application(mocked_logger, [mocked_command])
                application.run()
