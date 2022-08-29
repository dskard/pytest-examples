import pytest


class TestA:

    @pytest.fixture(autouse=True)
    def fixture1(self, request):
        print(f'{request.node.full_test_name} {request.fixturename} setup')
        yield
        print(f'{request.node.full_test_name} {request.fixturename} teardown')

    def test1(self, request):
        print(f'{request.full_test_name} call')
        assert True

    def test2(self, request):
        print(f'{request.full_test_name} call')
        assert False
