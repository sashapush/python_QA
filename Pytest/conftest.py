import pytest


@pytest.fixture(scope="class")  # this way it runs 1 time before tests start in class
def setup():
    print("At first i'm executing setup method")
    yield
    print("Checking is done, clearing resources")  # and 1 time after all tests are executed


# @pytest.fixture() will run fixture individually for each test


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Axel", "Sterling", "Site"]


# running test with multiple datasets
#@pytest.fixture(params=["chrome", "Firefox", "IE"]) #simple parametrized example
@pytest.fixture(params=[("chrome", "number1"), ("Firefox", "number 2",), "IE"]) #more complex parametrized example
def crossBrowsers(request):  # request is the param called from the list above
    return request.param
