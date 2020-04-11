import logging


def run_deprecate_func():
    from auto_deprecator_example.deprecate_from_utils.func import (
        warn_from_utils,
        warn_from_utils_and_module_version,
    )

    print('===============================================================')
    print('Current version = 1.0.0')
    print('===============================================================')
    print('Warning (Current version = 1.0.0, Expiry = 2.0)')
    print('===============================================================')
    warn_from_utils()
    print('===============================================================')
    print('Warning (Current version from module, Expiry = 2.0)')
    print('===============================================================')
    warn_from_utils_and_module_version()

    try:
        from auto_deprecator_example.deprecate_from_utils.func import (
            error_with_warning_handler,
        )
        print('===============================================================')
        print('Error with warning handler (Current version from module, Expiry = 2.0)')
        print('===============================================================')
        error_with_warning_handler()
        print('===============================================================')
    except ImportError:
        print('Function error_with_warning_handler is deprecated')


def run_deprecate_class():
    from auto_deprecator_example.deprecate_from_utils.classes import (
        TestClassA
    )

    print('===============================================================')
    print('Warning (Current version = 1.0.0, Expiry = 2.0)')
    print('===============================================================')
    TestClassA.TestClassB().c
    try:
        print('===============================================================')
        TestClassA.TestClassD().d()
        print('===============================================================')
    except AttributeError:
        print('TestClass D is depcreated')



def main():
    run_deprecate_func()
    run_deprecate_class()

if __name__ == '__main__':
    logging.basicConfig()
    main()
