from pycin.languages import Language


class PHP(Language):
    def __init__(self):
        super().__init__('php', 'PHP')

    def get_supported_tools(self):
        return []
