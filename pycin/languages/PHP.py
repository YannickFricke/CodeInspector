from PyInquirer import prompt

from pycin.definitions.FileSystem import FileSystem
from pycin.languages import Language
from pycin.package_manager.Composer import Composer
from pycin.supported_tools.php.PHPCS import PHPCS

pretty_name = 'PHP'


class PHP(Language):
    def __init__(self):
        super().__init__(
            'php',
            pretty_name,
            [
                Composer()
            ]
        )

    def setup(self, rootpath: str):
        questions = [
            {
                'type': 'list',
                'name': 'source_root',
                'message': 'Please select your directory ' +
                           'with the PHP sources',
                'choices': FileSystem.get_filtered_directories(rootpath)
            }
        ]

        questions.extend(self.get_questions_for_supported_tools())
        answers = prompt(questions)

        using_tools = []

        for key in answers.keys():
            if key == 'source_root':
                continue

            if answers[key]:
                using_tools.append(key)

        return {
            'sources': answers['source_root'],
            'tools': using_tools
        }

    def get_supported_tools(self):
        return [
            PHPCS()
        ]

    @staticmethod
    def get_pretty_name():
        return pretty_name
