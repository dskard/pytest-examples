import logging
import pytest

LOG = logging.getLogger()


@pytest.fixture(scope="function")
def teardown(request):
    """Register the cleanup of a resource after the test case completes

    The general format for registering a teardown is:

        teardown.register(lambda: fxn(args, kwargs))

    Examples:

        arg1 = "arg1"
        teardown.register(lambda: f1(arg1, "arg2"))
    """

    class TearDown:
        def __init__(self):
            self.teardowns = []

        def register(self, fxn):
            self.teardowns.append(fxn)

    teardown = TearDown()

    yield teardown

    # loop through all of the registered teardown requests.
    # perform the cleanup associated with each request.
    for t in reversed(teardown.teardowns):
        t()


def t1(a1, a2, a3):
    LOG.warning(f"a1 = {a1}, a2 = {a2}, a3 = {a3}")
