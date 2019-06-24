import pytest
from unittest.mock import MagicMock
from Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


def test_can_calculate_total(checkout):
    checkout.add_item("a")
    assert checkout.calculate_total() == 1


def test_get_correct_total_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


# @pytest.mark.skip  # use this decorator if we want to skip the unit test
# below.
def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.add_item("c")


# Create a unit test that sets up a mock of the Python open call which returns
# a mock file object.
#
# I'll set up that file object to return one line when it's iterated over: That
# one line will specify c 3.
#
# Verify that the open call was made properly, and that the new item price was
# added successfully, by adding that item to the checkout, and verifying the
# new total.
def test_verify_read_prices_from_file(checkout, monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["c 3"]
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    checkout.read_prices_from_file("testfile")
    checkout.add_item("c")
    result = checkout.calculate_total()
    mock_open.assert_called_once_with("testfile")
    assert result == 3
