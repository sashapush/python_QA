import requests
from behave import *

from api.BackEndAutomation.payloads import addBookPayload
from api.BackEndAutomation.utils import configs
from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources


@given("Book details which needs to be added to library")
def step_impl(
        context):  # context is global, context is object which can be assigned properties to be used across BDD,
    context.url = getConfig()['API']['endpoint'] + apiResources.addBook  # we're assigning a new property to this object
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("zxczxcxzcqzxa", "443")


@when('We execute  addBook POST method')
def step_impl(context):  # context is object which can be assigned properties to be used across BDD
    # query = "SELECT b.* from books b ORDER BY b.BookName desc;"
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers)
    print(context.response.status_code)
    assert context.response.status_code == 200
    print("Assert success - status code 200")


@then('Book is successfully added')
def step_impl(context):  # context is object which can be assigned properties to be used across BDD
    r = context.response.json()
    print(r)
    context.bookId = r["ID"]
    print(context.bookId)
    assert r["Msg"] == "successfully added"


@given("Book details with {isbn} and {aisle} to be added to library")
def step_impl(
        context, isbn,
        aisle):  # context is global, context is object which can be assigned properties to be used across BDD,
    context.url = getConfig()['API']['endpoint'] + apiResources.addBook  # we're assigning a new property to this object
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle)


@given(u'I have github credentials')
def step_impl(context):
    context.session = requests.session()  # creates a session stream
    context.session.auth = auth = ("sashapush@tut.by", configs.getPassword())


@when(u'I hit getRepositories API method')
def step_impl(context):
    context.response = context.session.get(apiResources.gitHubRepo)


@then(u'Status code of response is {statusCode:d}')
def step_impl(context, statusCode):
    print("\nGit got status code: ", context.response.status_code)
    assert context.response.status_code == statusCode
