import requests

from api.BackEndAutomation.payloads import *  # import * imports all methods instead of specific one

post_response = requests.post("http://216.10.245.166/Library/Addbook.php", json=addBookPayload("stabletest2"),
                              headers={"Content-Type": "application/json"})
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
delete_response = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={
    "ID": bookId}, headers={"Content-Type": "application/json"})
print(delete_response.status_code)
print(delete_response.text)
d = delete_response.json()
assert delete_response.status_code == 200
print("Assert success - status code 200")
assert d["msg"] == "book is successfully deleted"
