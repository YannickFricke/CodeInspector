from pycin.supported_tools import SupportedTool


class PHPCS(SupportedTool):
    def __init__(self):
        super().__init__(
            'phpcs',
            'PHP Coding Standards',
            'phpcs'
        )

    def execute(self, path: str):
        pass
