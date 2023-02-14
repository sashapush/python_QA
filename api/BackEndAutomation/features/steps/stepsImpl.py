import requests
from behave import *

from api.BackEndAutomation.payloads import addBookPayload
from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources


@given("Book details which needs to be added to library")
def step_implementation(
        context):  # context is global, context is object which can be assigned properties to be used across BDD,
    context.url = getConfig()['API']['endpoint'] + apiResources.addBook  # we're assigning a new property to this object
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("123")


@when('We execute  addBook POST method')
def step_impl(context):  # context is object which can be assigned properties to be used across BDD
    query = "SELECT b.* from books b ORDER BY b.BookName desc;"
    context.post_response = requests.post(context.url, json=context.payLoad, headers=context.headers)
    print(context.post_response.status_code)
    assert context.post_response.status_code == 200
    print("Assert success - status code 200")


@then('Book is successfully added')
def step_impl(context):  # context is object which can be assigned properties to be used across BDD
    r = context.post_response.json()
    print(r)
    bookId = r["ID"]
    print(bookId)
    assert r["Msg"] == "successfully added"
