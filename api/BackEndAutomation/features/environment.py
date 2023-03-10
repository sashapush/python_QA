import requests

from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources


# how to run Allure report
# behave .\api\BackEndAutomation\features\ --no-capture -f allure_behave.formatter:AllureFormatter -o api\AllureReports

def before_scenario(context, scenario):
    print("Run Before Each Scenario")


def after_scenario(context, scenario):
    if "books" in scenario.tags:  # we check the tag of scenario
        delete_url = getConfig()['API']['endpoint'] + apiResources.deleteBook
        delete_response = requests.post(delete_url, json={
            "ID": context.bookId}, headers={"Content-Type": "application/json"})
        print(delete_response.status_code)
        print(delete_response.text)
        d = delete_response.json()
        assert delete_response.status_code == 200
        print("Assert success - status code 200")
        assert d["msg"] == "book is successfully deleted"
