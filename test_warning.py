def run_deprecate_from_utils():
    from auto_deprecator_example.deprecate_from_utils.func import (
        warn_from_utils,
        warn_from_utils_and_module_version
    )

    print('===============================================================')
    print('Current version = 1.0.0')
    print('===============================================================')
    print('Warn from utils (Current version = 1.0.0, Expiry = 2.0)')
    print('===============================================================')
    warn_from_utils()
    print('===============================================================')
    print('Warn from utils (Current version from module, Expiry = 2.0)')
    warn_from_utils_and_module_version()
    print('===============================================================')


def main():
    run_deprecate_from_utils()

if __name__ == '__main__':
    main()
