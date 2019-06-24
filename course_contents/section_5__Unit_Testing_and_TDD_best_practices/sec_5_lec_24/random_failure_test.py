import random


count = 1


# Here we have a contrived example of when unit_tests might fail / succeed.
def test_fail_randomly():
    random.seed()
    assert random.randint(1, 100) % 2 == 0
