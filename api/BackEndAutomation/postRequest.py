import requests
from api.BackEndAutomation.payloads import *  # import * imports all methods instead of specific one
from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources
import os

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

# Authentication to github
# print(os.environ)
ass = os.environ.get('GPASS')
gurl = 'https://api.github.com/user'
git_response = requests.get(gurl, auth=("sashapush@tut.by", ass))  # attribute verify=False will skip ssl sertificate
print("Git got status code: ", git_response.status_code)

# TODO more testing with httpbin.org
url = 'https://httpbin.org/post'
files = {'file': open('Library-API.docx', 'rb')}
r = requests.post(url, files=files)
print(r.text)
