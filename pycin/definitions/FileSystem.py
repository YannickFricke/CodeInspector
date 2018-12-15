import os


class FileSystem:
    @staticmethod
    def get_directories(path):
        return list(filter(lambda item: os.path.isdir(item), os.listdir(path)))
