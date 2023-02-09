import json

import requests

r = requests.get("http://216.10.245.166/Library/GetBook.php",
                 params={"AuthorName": "Apushka"})  # .get is used for get method, .post for post etc
# print(r.text) #text
print(r.status_code)
# print(r.request) #GET
assert r.status_code == 200
# print(type(r.text)) #text is string
# print(type(r.content)) #content is bytes
# r_json = json.loads(r.text)  # returns as list, not dictionary. Can be optimised
# New approach:
new_r = r.json()  # converts to list with 1 simple step
print(type(new_r))  # list
print(new_r)
for actual_book in new_r:
    if actual_book["book_name"] == "Look for a dream job":
        print(actual_book["isbn"])
        assert actual_book["aisle"] == "227"
        # assert_book = actual_book #store needed book for further assertion.
        # alternatively we can break our of this condition
        break
    if actual_book["book_name"] == "Look":
        print(actual_book["isbn"] + " " + actual_book["aisle"])
        print(actual_book)  # or we can get item's data as a whole
        assert actual_book["aisle"] == "2271"
expected_book = {
    "book_name": "Look for a dream job",
    "isbn": "aqa",
    "aisle": "227"
}
print(r.headers)
assert actual_book == expected_book
# assert assert_book == expected_book
# header Content-Type = 'application/json;charset=UTF-8'
assert r.headers["Content-Type"] == "application/json;charset=UTF-8"
print("Assert success: Content-Type = application/json;charset=UTF-8")
# r_bytes = r.content
