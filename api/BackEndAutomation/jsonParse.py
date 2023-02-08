import json

# json library is used for deserialising json
json_file = '{"name": "Axel","languages":["Java","Python"]}'

# loads parses json string to dictionary;
ass = json.loads(json_file)
print(type(ass))  # dictionary
print(ass)
print(ass["name"])
print(ass["languages"])  # returns list
print(ass["languages"][0])  # returns values
