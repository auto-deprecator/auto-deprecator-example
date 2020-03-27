from auto_deprecator_example.utils.auto_deprecator.deprecate import deprecate


class TestClassA:

    class TestClassB:

        @property
        def b(self):
            return 'b'

        @property
        @deprecate(expiry='2.0.0', version_module=__name__.split('.')[0])
        def c(self):
            return 'c'

    class TestClassD:

        @property
        @deprecate(expiry='1.0.0', version_module=__name__.split('.')[0],
                   error_handler=print)
        def d(self):
            return 'c'
