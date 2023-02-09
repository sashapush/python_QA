import requests
from api.BackEndAutomation.payloads import *  # import * imports all methods instead of specific one
from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources

url = getConfig()['API']['endpoint'] + apiResources.addBook
headers = {"Content-Type": "application/json"}

post_response = requests.post(url,
                              json=addBookPayload("stabletest2"),
                              headers=headers)
print(post_response.status_code)
# print(response.content) #bytes
assert post_response.status_code == 200
print("Assert success - status code 200")
# print(post_response.text)
r = post_response.json()
# print(type(r)) #now it's dictionary
print(r)
bookId = r["ID"]
# print(bookId)

#
delete_url = getConfig()['API']['endpoint'] + apiResources.deleteBook
delete_response = requests.post(delete_url, json={
    "ID": bookId}, headers=headers)
print(delete_response.status_code)
print(delete_response.text)
d = delete_response.json()
assert delete_response.status_code == 200
print("Assert success - status code 200")
assert d["msg"] == "book is successfully deleted"
