from auto_deprecator import deprecate


@deprecate(expiry='2.0.0', version_module='auto_deprecator_example')
def old_hello_world():
    return print("Hello world!")


def hello_world():
    return print("Hello world again!")
