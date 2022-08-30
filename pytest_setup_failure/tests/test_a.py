import os
import pytest


@pytest.fixture(scope='function')
def fix3():
    print('')
    print('setup 3')
    with open("fff", "w") as f:
        f.write("fff")
    yield
    print('teardown 3')
    os.remove("fff")


@pytest.fixture(scope='function')
def fix2():
    print('setup 2')
    with open("ggg", "w") as f:
        f.write("ggg")
    yield
    print('')
    print('teardown 2')
    os.remove("ggg")


@pytest.fixture(scope='function')
def fix1(fix2):
    print('setup 1')
    #raise Exception('test 1 setup exception')
    #pytest.fail('test 1 setup exception')
    assert False
    yield
    print('teardown 1')


def test1(fix3, fix1):
    print('test 1')
