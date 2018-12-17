from pathlib import Path

from pycin.package_manager import PackageManager


class Composer(PackageManager):
    def __init__(self):
        super().__init__(
            'composer',
            'Composer',
            'vendor/bin/',
            '{}/.composer/vendor/bin/'.format(Path.home())
        )
