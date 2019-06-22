import pytest


def raise_value_exception():
    raise ValueError


def test_exception():
    with pytest.raises(ValueError):
        raise_value_exception()
