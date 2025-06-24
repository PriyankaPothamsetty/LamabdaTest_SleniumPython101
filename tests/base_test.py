import pytest

# Applying the 'usefixtures' marker to the entire class.
# This ensures that the 'initialize_driver' fixture is automatically used for all test methods in this class.
@pytest.mark.usefixtures("setup_teardown")
class BaseTest:
    """
    BaseTest class serves as a parent class for test cases that require a web driver setup.
    The 'setup_teardown' fixture will be applied to all tests inheriting from this class. setup_teardown
    """
    pass