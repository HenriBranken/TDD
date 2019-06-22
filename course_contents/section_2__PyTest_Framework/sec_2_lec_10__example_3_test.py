import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)
    # here we specify two different teardown functions.
    # Multiple finalization functions can be specified.
    # request.addfinalizer() is somewhat more capable.


def test1(setup1):
    print("Executing test1")
    assert True


def test2(setup2):
    print("Executing test2")
    assert True
