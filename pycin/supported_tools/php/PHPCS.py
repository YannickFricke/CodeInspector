import json
import linecache
import subprocess
from json import JSONDecodeError
from typing import List

from pycin.definitions.FileSystem import FileSystem
from pycin.package_manager import PackageManager
from pycin.supported_tools import SupportedTool


class PHPCS(SupportedTool):
    def __init__(self):
        super().__init__(
            'phpcs',
            'php Coding Standards',
            'phpcs'
        )

    def execute(self,
                path: str,
                package_managers: List[PackageManager]):
        found_binary = FileSystem().get_binary_path(self.executable, package_managers)

        if found_binary is None:
            raise Exception(
                'The binary {} for {} ({}) could not be found'.format(
                    self.executable,
                    self.name,
                    self.pretty_name,
                )
            )

        response = subprocess.run(
            [
                found_binary,
                '--report=json',
                path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        returncode = response.returncode

        if returncode != 0 and returncode != 2:
            return False

        try:
            parsed_json = json.loads(str(response.stdout, 'utf-8'))
        except JSONDecodeError:
            raise Exception(
                'Could not parse json from the output of {} ({})'.format(
                    self.name,
                    self.pretty_name
                )
            )

        for file, file_informations in parsed_json['files'].items():
            for message in file_informations['messages']:

                if file in self.errors:
                    self.errors[file].append(self.get_error_dict(
                        message['message'],
                        message['line'],
                        linecache.getline(file, message['line'])
                    ))
                else:
                    self.errors[file] = [
                        self.get_error_dict(
                            message['message'],
                            message['line'],
                            linecache.getline(file, message['line'])
                        )
                    ]

        return True
