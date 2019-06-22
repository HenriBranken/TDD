from pytest import approx


# This is how the code in `sec_2_lec_11__example_3_test.py` should have been
# rectified.
def test_float():
    assert (0.1 + 0.2) == approx(0.3)
