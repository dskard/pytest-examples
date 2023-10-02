import logging
import pytest

from .conftest import t1

LOG = logging.getLogger()


def t2(arg1):
    LOG.debug(f"arg1 = {arg1}")


class Obj:
    def __init__(self, v1):
        self.v1 = v1


class TestCases:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.arg3 = Obj("my obj")

    def test1(self, teardown):
        arg2 = {"a": 1, "b": 2}
        teardown.register(lambda: t1("this is t1", arg2, self.arg3))
        teardown.register(lambda: t2("this is t2"))
        assert True
