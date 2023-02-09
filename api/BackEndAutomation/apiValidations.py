import json

import requests

r = requests.get("http://216.10.245.166/Library/GetBook.php",
                 params={"AuthorName": "Apushka"})  # .get is used for get method, .post for post etc
print(r.text)
print(r.status_code)
# print(type(r.text)) #text is string
# print(type(r.content)) #content is bytes
r_json = json.loads(r.text)  # returns as list, not dictionary. Can be optimised
# iterate through list


# New approach:
new_r = r.json()  # converts to list with 1 simple step
print(type(new_r))  # list
print(new_r)
for item in new_r:
    if item["book_name"] == "Look for a dream job":
        print(item["isbn"])
        assert item["aisle"] == "227"
    if item["book_name"] == "Look":
        print(item["isbn"] + " " + item["aisle"])
        assert item["aisle"] == "2271"

r_bytes = r.content
