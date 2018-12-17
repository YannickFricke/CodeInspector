class PackageManager:
    def __init__(self,
                 name: str,
                 pretty_name: str,
                 binary_directory: str,
                 global_binary_directory: str
                 ):
        self.name = name
        self.pretty_name = pretty_name
        self.binary_directory = binary_directory
        self.global_binary_directory = global_binary_directory

    def __str__(self):
        return self.pretty_name
