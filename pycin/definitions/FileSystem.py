import os


class FileSystem:
    @staticmethod
    def get_directories(path: str):
        """
        Returns all directories for the given path
        :param path: The path where to check for the directories
        :return: The directories in the path
        """
        return list(filter(lambda item: os.path.isdir(item), os.listdir(path)))
