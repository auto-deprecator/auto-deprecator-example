from auto_deprecator import deprecate


@deprecate(expiry='2.0.0', current='1.9.0')
def old_hello_world():
    return print("Hello world!")


def hello_world():
    return print("Hello world again!")
