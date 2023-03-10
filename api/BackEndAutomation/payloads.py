from api.BackEndAutomation.utils.configs import getQuery


def addBookPayload(isbn, aisle):
    body = {
        "name": "testing",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Apushka"
    }
    return body


def buildPayloadFromDB(query):
    addBody = {}
    record = getQuery(query)  # tuple
    addBody["name"] = record[0]  # value from DB
    addBody["isbn"] = record[1]
    addBody["aisle"] = record[2]
    addBody["author"] = record[3]

    return addBody
