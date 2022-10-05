import os
import pytest


@pytest.fixture(scope='function', autouse=True)
def fix4():
    print('')
    print('setup 4')
    yield
    print('teardown 4')


@pytest.fixture(scope='function')
def fix3():
    print('setup 3')
    yield
    print('teardown 3')


@pytest.fixture(scope='function')
def fix2():
    print('setup 2')
    yield
    print('teardown 2')


@pytest.fixture(scope='function')
def fix1(fix2):
    print('setup 1')
    yield
    print('teardown 1')


def test1(fix3, fix1):
    print('test 1')
    assert False
