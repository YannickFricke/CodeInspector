import logging
import sys

from dependency_injector import containers, providers

from pycin.commands.InitCommand import InitCommand
from pycin.definitions.Application import Application


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
    logger = providers.Object(get_configured_logger())

    initCommand = providers.Singleton(InitCommand, logger)

    known_commands = [
        initCommand()
    ]

    application = providers.Factory(Application, logger, known_commands)
