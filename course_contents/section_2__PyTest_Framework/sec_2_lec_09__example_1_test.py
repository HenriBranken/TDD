def setup_module():
    # Called only once before any of the unit tests in the module are being
    # executed.
    print("Setting up the module.")


def teardown_module():
    # Called only once after all of the unit tests in the module have completed
    # execution.
    print("Tearing down the module.")


def setup_function(function):
    # pytest will automatically call setup_function before EACH unit test in
    # that module that is not in a class.
    if function == test1:
        print("\nSetting up test1.")
    elif function == test2:
        print("\nSetting up test2.")
    else:
        print("\nSetting up unknown test.")


def teardown_function(function):
    # pytest will automatically call teardown_function after EACH unit test has
    # completed executing
    if function == test1:
        print("\nTearing down test1.")
    elif function == test2:
        print("\nTearing down test2.")
    else:
        print("\nTearing down unknown test.")

# setup_function and teardown_function are being passed in the unit test that
# is being executed, and so the setup and teardown code can be customised per
# unit test if necessary.


def test1():
    print("Executing test1.")
    assert True


def test2():
    print("Executing test2.")
    assert True
