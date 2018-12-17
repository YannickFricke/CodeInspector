import logging
import sys

from dependency_injector import containers, providers

from pycin.code_provider.GitHub import GitHub
from pycin.commands.InitCommand import InitCommand
from pycin.definitions.Application import Application
from pycin.languages.PHP import PHP


def get_configured_logger():
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(
        logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s',
            '%d.%m.%Y %H:%M:%S'
        )
    )

    configured_logger = logging.Logger('PyCin')
    configured_logger.setLevel(logging.DEBUG)
    configured_logger.addHandler(stdout_handler)

    return configured_logger


class Container(containers.DynamicContainer):
    # Logging

    logger = providers.Object(get_configured_logger())

    # Commands

    supported_languages = [
        PHP()
    ]

    supported_code_providers = [
        GitHub
    ]

    initCommand = providers.Singleton(InitCommand,
                                      logger,
                                      supported_languages,
                                      supported_code_providers)

    # The application

    known_commands = [
        initCommand()
    ]

    application = providers.Factory(Application, logger, known_commands)
