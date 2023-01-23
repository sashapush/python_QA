import pytest
from Pytest.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad):
        #print(f"Name is  {dataLoad[0]}")
        log = self.getLogger()
        #we're replacing the print with logging via log object, taken from BaseClass.getLogger()
        log.info(f"Name is  {dataLoad[0]}")
        log.info(f"Surname is {dataLoad[1]}")
        log.info(f"Site is {dataLoad[2]}")
        #print(f"Surname is {dataLoad[1]}")
        #print(f"Site is {dataLoad[2]}")
