import json

# json library is used for deserialising json
json_file = '{"name": "Axel","languages":["Java","Python"]}'

# loads parses json **string** to dictionary;
# ass = json.loads(json_file) #.loads to parse string
# print(type(ass))  # dictionary
# print(ass)
# print(ass["name"])
# print(ass["languages"])  # returns list
# print(ass["languages"][0])  # returns values


# parse json file**
with open(
        "/api/BackEndAutomation/ass.json") as f:  # without param it opens in read mode
    file = json.load(f)  # we create a new dictionary from file
    print(type(file))  # dictionary
    # print(file) #file content
    # print(file["result"]["chart"][1]["score"])
    # print(file["result"])
    # get the result for the exact date key "2021-12-18", not index. Value is 76
    # print(type(file["result"]["chart"]))  # list
    # to get this result we iterate through the file
    for item in file["result"]["chart"]:
        if item["dt"] == "2021-12-18":
            print(item["score"])
            assert item["score"] == 76.0
    # print(file["result"]["chart"])
# compare 2 json files - open both files and store to dictionareis
with open("/api/BackEndAutomation/as2.json") as fi:
    file2 = json.load(fi)
    print(file, "\n", file2)
    print(file == file2)  # this is how we compare files, returns False
