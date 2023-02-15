import requests
from api.BackEndAutomation.payloads import *  # import * imports all methods instead of specific one
from api.BackEndAutomation.utils import configs
from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.resources import apiResources

url = getConfig()['API']['endpoint'] + apiResources.addBook
headers = {"Content-Type": "application/json"}
# query = buildPayloadFromDB("SELECT b.* from books b ORDER BY b.BookName desc;")
query = "SELECT b.* from books b ORDER BY b.BookName desc;"
# post_response = requests.post(url, json=query, headers=headers)
post_response = requests.post(url, json=buildPayloadFromDB(query), headers=headers)
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

# Get book by author endpoint
author = "Sasha pushka"
get_url = getConfig()['API']['endpoint'] + apiResources.getBookByAuthorName + author
get_response = requests.get(get_url)
print(get_response.status_code)
assert get_response.status_code == 200
g = get_response.json()
print(f"Getting the book list of an {author}: ", g)

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
# ass = os.environ.get('GPASS')
# Let's create a session
session = requests.session()  # creates a session stream
session.auth = auth = ("sashapush@tut.by", configs.getPassword())
gurl = 'https://api.github.com/user'
git_response = session.get(gurl)  # attribute verify=False will skip ssl certificate /or use getPassword() instead opf
print("\nGit got status code: ", git_response.status_code)

# TODO more testing with httpbin.org
url = 'https://httpbin.org/post'
files = {'file': open('Library-API.docx', 'rb')}
r = requests.post(url, files=files)
#print(r.text) returns uploaded file from response

# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user
gurl2 = gurl + "/repos"
gr = session.get(gurl2)  # will not work without auth - session was created
# alternatively - gr = session.get(gurl2,auth=("sashapush@tut.by", configs.getPassword())) shitty way to do itL
print(gr.status_code)
#print(gr.text)
