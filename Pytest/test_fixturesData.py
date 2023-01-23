import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        print(f"Name is  {dataLoad[0]}")
        print(f"Surname is {dataLoad[1]}")
        print(f"Site is {dataLoad[2]}")
