import logging
import os
from typing import List

from PyInquirer import prompt
from yaml import dump

from pycin.code_provider import CodeProvider
from pycin.commands import Command
from pycin.definitions.FileSystem import FileSystem, CONFIG_FILE_NAME
from pycin.languages import Language


class InitCommand(Command):
    def __init__(self,
                 logger: logging.Logger,
                 supported_languages: List[Language],
                 supported_code_providers: List[CodeProvider]):
        """
        Initializes the InitCommand
        """
        super().__init__('init')
        self.logger = logger
        self.path = ''
        self.supported_languages = supported_languages
        self.supported_code_providers = supported_code_providers

    def execute(self, arguments: List[str]):
        """
        Executes the InitCommand
        :param arguments: The arguments for the execution of the command
        :return: True on success. Otherwise false.
        """

        if len(arguments) == 0:
            self.path = FileSystem.ensure_trailing_path_seperator(os.getcwd())
        else:
            self.path = FileSystem.ensure_trailing_path_seperator(
                os.path.realpath(arguments[0])
            )

        self.logger.info('Initializing in "%s"!', self.path)

        used_languages = self.prompt_for_used_languages()

        if len(used_languages) == 0:
            self.logger.warning(
                'No languages selected. Aborting initialization.'
            )
            return True

        configuration_contents = self.setup_languages(used_languages)

        used_code_providers = self.prompt_for_used_code_providers()
        configuration_contents['providers'] = self.setup_code_providers(
            used_code_providers
        )

        config_file_handle = os.open(
            self.path + CONFIG_FILE_NAME,
            os.O_CREAT | os.O_WRONLY
        )
        os.write(
            config_file_handle,
            bytes(
                dump(
                    configuration_contents,
                    default_flow_style=False),
                encoding='utf-8'
            )
        )
        os.close(config_file_handle)

        return True

    def setup_languages(self, languages: List[str]):
        configuration = {}

        for supported_language in self.supported_languages:
            if supported_language.pretty_name not in languages:
                continue

            configuration[supported_language.name] = []
            configuration[supported_language.name].append(
                supported_language.setup(self.path)
            )

        return configuration

    def setup_code_providers(self, used_code_providers):
        configuration = {}

        questions = []

        for supported_code_provider in self.supported_code_providers:
            if supported_code_provider.get_pretty_name() \
                    not in used_code_providers:
                continue

            questions.append({
                'type': 'input',
                'name': supported_code_provider.get_name(),
                'message': 'Please enter the url of {}'.format(
                    supported_code_provider.get_pretty_name()
                ),
            })

        urls = prompt(questions)

        for supported_code_provider in self.supported_code_providers:
            if supported_code_provider.get_name() not in urls:
                continue

            configuration[supported_code_provider.get_name()] = urls[
                supported_code_provider.get_name()
            ]

        return configuration

    def prompt_for_used_languages(self):
        """
        Prompts the user for the used languages in the project
        :return: The pretty names of the used languages
        """
        question = [
            {
                'type': 'checkbox',
                'name': 'languages',
                'message': 'Select the used languages',
                'choices': self.get_list_as_choices(self.supported_languages)
            }
        ]

        return prompt(question)['languages']

    def prompt_for_used_code_providers(self):
        question = [
            {
                'type': 'checkbox',
                'name': 'code_providers',
                'message': 'Select the used code providers',
                'choices': self.get_list_as_choices(
                    self.supported_code_providers
                )
            }
        ]

        return prompt(question)['code_providers']

    def get_list_as_choices(self, list_to_process):
        """
        Returns a list of dictionaries of the supported languages
        for PyInquirer
        :return: The list of dictionaries
        """
        result = []

        for entry in list_to_process:
            result.append({
                'name': entry.get_pretty_name()
            })

        return result
