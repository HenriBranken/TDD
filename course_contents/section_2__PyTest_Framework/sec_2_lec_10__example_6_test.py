import pytest


# powerful and easy way to run the unit test with various values.
@pytest.fixture(params=[1, 2, 3])
def setup(request):
    ret_val = request.param
    print("\nSetup ret_val = {}.".format(ret_val))
    return ret_val


def test_1(setup):
    print("\nsetup = {}.".format(setup))
    assert True
