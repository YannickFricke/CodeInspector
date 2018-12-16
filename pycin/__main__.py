import sys

from pycin.definitions.Application import Application
from pycin.definitions.Container import Container

if len(sys.argv) < 2:
    print('No command specified')
    Application.display_help()
    sys.exit(1)

container = Container()
container.application().run()
