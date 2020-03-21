from auto_deprecator_example import __version__

from auto_deprecator_example.utils.auto_deprecator.deprecate import deprecate

@deprecate(expiry='2.0', current=__version__)
def warn_from_utils():
    print('It is a warning from utils')


@deprecate(expiry='2.0', version_module='auto_deprecator_example')
def warn_from_utils_and_module_version():
    print('It is a warning and the version is derived from the module')
