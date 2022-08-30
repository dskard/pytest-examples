# pytest_setup_failure

This example shows that even if there is a failure in the setup phase of a fixture, the teardown phases of fixtures that previously ran will still be executed. The test case depends on fixtures `fix3` and `fix1`. Fixture `fix1` depends on fixture `fix2`.

The order of execution is:
1. `test1` starts dependency `fix3`.
2. `fix3` is executed and yields.
3. `test1` starts dependency `fix1`.
4. `fix1` starts its dependency `fix2`.
5. `fix2` executes and yields.
6. `fix1` executes and errors.
7. `fix2` resumes and exits.
8. `fix3` resumes and exits.

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
make test PYTESTOPS="-s -qq"
```

You'll get output that looks like this:
```
poetry run pytest \
    --verbose \
    --tb=short \
    -s -qq

setup 3
setup 2
setup 1
E
teardown 2
teardown 3

========================================= ERRORS =========================================
________________________________ ERROR at setup of test1 _________________________________
tests/test_a.py:32: in fix1
    assert False
E   assert False
================================ short test summary info =================================
ERROR tests/test_a.py::test1 - assert False
1 error in 0.08s
```

Clean logs and Python cache files
```bash
make clean
```
