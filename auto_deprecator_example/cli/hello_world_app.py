"""Hello world app.

Usage:
    hello-world-app [options]

Options:
    -v, --version       Display version.
"""  # noqa
from docopt import docopt

from auto_deprecator_example import __version__
from auto_deprecator_example.deprecate_from_package.doc_example import (
    old_hello_world
)


def main():
    args = docopt(__doc__, version=__version__)
    old_hello_world()
