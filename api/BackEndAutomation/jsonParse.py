import json

# json library is used for deserialising json
json_file = '{"name": "Axel","languages":["Java","Python"]}'

# loads parses json **string** to dictionary;
# ass = json.loads(json_file)
# print(type(ass))  # dictionary
# print(ass)
# print(ass["name"])
# print(ass["languages"])  # returns list
# print(ass["languages"][0])  # returns values


# parse json file**
with open(
        "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\ass.json") as f:  # without param it opens in read mode
    file = json.load(f)  # we create a new dictionary from file
    print(type(file))  # dictionary
    # print(file) #file content
    print(file["result"]["chart"][1]["score"])
    print(file["result"])
