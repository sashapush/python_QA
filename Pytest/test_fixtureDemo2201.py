import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I am running steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I am running steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I am running steps in fixtureDemo3 method")

    def test_fixtureDemo4(self):
        print("I am running steps in fixtureDemo4 method")

#in order not to call fixture every time for each test - tests can be added to class, and declare fixture on class level
