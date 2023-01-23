# any pytest test should be named test_balalalal or end with  blalblbl_test
# method should be declared with test_
# any code should be wrapped in method
# py.test params: -k runs specific method names by mask, -v for more info, -s for logs in output
# pytest.mark.name -> cmd py.test -m name -v -s runs only tests with this mark
# to skip a test add the following mark @pytest.mark.skip
# failing tests can still be executed(f.e. as preconditions) but not be marked in the report @pytest.mark.xfail
# fixtures can be set with scope to Class and they will run on start and finish (if yield) of class tests

#def test_firstDemo(setup):
#    print("Hello from test")


#def test_failDemo(setup):
#    assert True == True, "Test Failed lolo"


# parametrization example below - with return statements in fixture
def test_crossBrowsers(crossBrowsers):
    print(crossBrowsers)
    print(crossBrowsers[0])
