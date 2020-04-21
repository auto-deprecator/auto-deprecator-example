import logging

from auto_deprecator_example import __version__

from auto_deprecator_example.utils.auto_deprecator import deprecate

LOGGER = logging.getLogger(__name__)


@deprecate(expiry='2.0', current='1.0')
def hello_world():
    print('Hello world')


@deprecate(expiry='2.0', current=__version__)
def warn_from_utils():
    print('It is a warning from utils')


@deprecate(expiry='2.0', version_module='auto_deprecator_example',
           relocate='another_method')
def warn_from_utils_and_module_version():
    print('It is a warning and the version is derived from the module')


@deprecate(expiry='1.0', version_module=__name__.split('.')[0],
           error_handler=LOGGER.warning)
def error_with_warning_handler():
    print('It is a expiry function  and the handler is the LOGGER.warn')
