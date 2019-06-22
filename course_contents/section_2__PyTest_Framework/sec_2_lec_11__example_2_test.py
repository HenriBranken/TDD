# We know for sure that the following test is going to fail.
# Internally does not exactly align with the expected value.


def test_float():
    assert (0.1 + 0.2) == 0.3
