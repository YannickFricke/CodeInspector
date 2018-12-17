import os
from abc import ABC, abstractmethod
from typing import List


class CodeProvider(ABC):
    def __init__(self,
                 url: str,
                 ):
        self.url = url

    @abstractmethod
    def comment_on_commit(self,
                          commit_id: str,
                          filename: str,
                          line: int,
                          comment: str
                          ):
        """

        :param commit_id:
        :param filename:
        :param line:
        :param comment:
        :return:
        """

    @abstractmethod
    def comment_on_merge_request(self,
                                 merge_request_id: str,
                                 commit_id: str,
                                 filename: str,
                                 line: int,
                                 comment: str
                                 ):
        """

        :param merge_request_id:
        :param commit_id:
        :param filename:
        :param line:
        :param comment:
        :return:
        """

    @staticmethod
    @abstractmethod
    def get_name():
        """
        Returns the name of this code provider
        :return: The name of the code provider
        """

    @staticmethod
    @abstractmethod
    def get_pretty_name():
        """
        Returns the pretty name of this code provider
        :return: The pretty name of the code provider
        """

    @staticmethod
    @abstractmethod
    def create_from_environment_variables(url: str):
        """
        Returns a valid instance from the environment variables
        :return: A valid instance of the code provider
        """

    @staticmethod
    def get_from_environment_with_list(list_to_process: List[str]):
        for envusername in list_to_process:
            read_variable = os.getenv(envusername)
            if read_variable is not None:
                return read_variable

        return None
