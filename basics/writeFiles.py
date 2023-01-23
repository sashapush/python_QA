#WRITE
#read the file and store all lines in list
#reverse the list
#write the list back to file

with open("blank.txt", "r") as file: #file is closed automatically via WITH operator
    content = file.readlines() #list is created from file data
    rev = reversed(content)
    with open("blank.txt", "w") as file:
        for line in rev:
            file.write(line)

ass = "pussy"
print(reversed(ass))
for item in reversed(ass):
    print(item)