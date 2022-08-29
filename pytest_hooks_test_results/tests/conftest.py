import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):

    full_test_name = (
        f"{item._request.node.module.__name__}"
        f".{item._request.node.cls.__name__}"
        f".{item._request.node.name}"
    )

    setattr(item, "full_test_name", full_test_name)
    setattr(item._request, "full_test_name", full_test_name)

    print(f"{item.full_test_name} setup hook before")

    yield

    print(f"{item.full_test_name} setup hook after")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_call(item):

    print(f"{item.full_test_name} call hook before")

    yield

    print(f"{item.full_test_name} call hook after")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item):

    print("")
    print(f"{item.full_test_name} teardown hook before")

    yield

    print(f"{item.full_test_name} teardown hook after")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # test cases have different phases.
    # the makereport hook is called after each phase and contains a phase status
    # phase of a test case include "setup", "call", "teardown"

    # i don't see people putting anything before the yield,
    # but i guess you could do something here
    print(f"{item.full_test_name} makereport hook before")

    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # the phase is in rep.when
    # the phase status is in rep.outcome
    print(f"{item.full_test_name} makereport hook after: {rep.when} {rep.outcome}")

    # typically i see people adding code to do
    # something after a phase passed or failed:
    if rep.when == "call":
        if rep.outcome == "passed":
            pass
        if rep.outcome == "failed":
            pass

    if rep.when == "teardown":
        print("")
