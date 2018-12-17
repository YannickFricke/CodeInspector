from github3 import login

from pycin.code_provider import CodeProvider

username_environment_variable_names = [
    'GH_USER',
    'GH_USERNAME',
]

password_environment_variable_names = [
    'GH_PASS',
    'GH_PASSWORD',
]

token_environment_variable_names = [
    'GH_TOKEN'
]


class GitHub(CodeProvider):
    def __init__(self,
                 url: str
                 ):
        super().__init__(url)
        self.client = None

    def login_with_username_and_password(self, username: str, password: str):
        self.client = login(username=username, password=password)

    def login_with_token(self, token: str):
        self.client = login(token=token)

    def comment_on_commit(self,
                          commit_id: str,
                          filename: str,
                          line: int,
                          comment: str):
        pass

    def comment_on_merge_request(self,
                                 merge_request_id: str,
                                 commit_id: str,
                                 filename: str,
                                 line: int,
                                 comment: str):
        pass

    @staticmethod
    def get_name():
        return 'github'

    @staticmethod
    def get_pretty_name():
        return 'GitHub'

    @staticmethod
    def create_from_environment_variables(url: str):
        username = CodeProvider.get_from_environment_with_list(
            username_environment_variable_names
        )
        password = CodeProvider.get_from_environment_with_list(
            password_environment_variable_names
        )
        token = CodeProvider.get_from_environment_with_list(
            token_environment_variable_names
        )

        github = GitHub(url)

        if username is not None and password is not None:
            github.login_with_username_and_password(username, password)
            return github
        elif token is not None:
            github.login_with_token(token)
            return github

        raise Exception(
            'Could not find any login informations from the'
            'environment variables'
        )
