import sys

from pycin.definitions.Container import Container

container = Container()

sys.exit(0 if container.application().run() else 1)
