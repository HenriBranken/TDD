# import pytest

# ALL TEST CASES SORTED BY ORDER OF INCREASING COMPLEXITY:
# Can call LeapYear.
# Return False for not divisible by 4.
# Returns True for divisible by 4, but not 100 or 400.
# Returns False for divisible by 4, but is divisible by 100 but not 400.
# Returns True for divisible by 4, divisible by 100, and divisible by 400.


def leap_year(year):
    if not (year % 4):
        if not (year % 100):
            if not (year % 400):
                return True
            return False
        return True
    return False


def check_leap_year(year, expected_result):
    ret_val = leap_year(year)
    assert ret_val == expected_result


def test_return_false_not_divisible_by_4():
    check_leap_year(1995, False)


def test_return_true_div_by_4_but_not_100_or_400():
    check_leap_year(1996, True)


def test_return_false_divisible_by_4_and_100():
    check_leap_year(2100, False)


def test_return_true_div_by_4_and_100_and_400():
    check_leap_year(2000, True)
