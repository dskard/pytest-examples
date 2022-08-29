# pytest_hooks_test_results

## Running this example

Create a Python virtual environment:
```bash
make pyenv
```
or use your favorite virtual environment tools, just be sure to install the `poetry` python package.

Installing the development dependencies and current version of the library:
```bash
make install
```

Running the test cases:
```bash
make test PYTESTOPS="-s"
```

You'll get output that looks like this:
```
poetry run pytest \
    --verbose \
    --tb=short \
    -s
==================================================================== test session starts =====================================================================
platform linux -- Python 3.9.11, pytest-7.1.2, pluggy-1.0.0 -- /home/zx/.cache/pypoetry/virtualenvs/pytest-hooks-test-results-yCHLeixh-py3.9/bin/python
cachedir: .pytest_cache
rootdir: /home/zx/playground/pytest/pytest_hooks_test_results
collected 2 items

tests/test_a.py::TestA::test1 tests.test_a.TestA.test1 setup hook before
tests.test_a.TestA.test1 fixture1 setup
tests.test_a.TestA.test1 setup hook after
tests.test_a.TestA.test1 makereport hook before
tests.test_a.TestA.test1 makereport hook after: setup passed
tests.test_a.TestA.test1 call hook before
tests.test_a.TestA.test1 call
tests.test_a.TestA.test1 call hook after
tests.test_a.TestA.test1 makereport hook before
tests.test_a.TestA.test1 makereport hook after: call passed
PASSED
tests.test_a.TestA.test1 teardown hook before
tests.test_a.TestA.test1 fixture1 teardown
tests.test_a.TestA.test1 teardown hook after
tests.test_a.TestA.test1 makereport hook before
tests.test_a.TestA.test1 makereport hook after: teardown passed


tests/test_a.py::TestA::test2 tests.test_a.TestA.test2 setup hook before
tests.test_a.TestA.test2 fixture1 setup
tests.test_a.TestA.test2 setup hook after
tests.test_a.TestA.test2 makereport hook before
tests.test_a.TestA.test2 makereport hook after: setup passed
tests.test_a.TestA.test2 call hook before
tests.test_a.TestA.test2 call
tests.test_a.TestA.test2 call hook after
tests.test_a.TestA.test2 makereport hook before
tests.test_a.TestA.test2 makereport hook after: call failed
FAILED
tests.test_a.TestA.test2 teardown hook before
tests.test_a.TestA.test2 fixture1 teardown
tests.test_a.TestA.test2 teardown hook after
tests.test_a.TestA.test2 makereport hook before
tests.test_a.TestA.test2 makereport hook after: teardown passed



========================================================================== FAILURES ==========================================================================
________________________________________________________________________ TestA.test2 _________________________________________________________________________
tests/test_a.py:18: in test2
    assert False
E   assert False
================================================================== short test summary info ===================================================================
FAILED tests/test_a.py::TestA::test2 - assert False
================================================================ 1 failed, 1 passed in 0.07s =================================================================
Makefile:26: recipe for target 'test' failed
make: *** [test] Error 1
```

Clean logs and Python cache files
```bash
make clean
```
