#read/write files
#READ
#with open("test.txt", 'r') as file:
#    print(file.read())
#    file.close()
#print("")
# OR
file = open("test.txt")
#print(file.read()) #reads all file
#print(file.read(4)) #reads 4 bytes #or NOT:)
#print(file.readline()) #reads first line
#print(file.readline()) #reads second line
#file.close()

#readline() - reads 1 line
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()


#readlines() - creates a list of lines
for line in file.readlines(): #iterate through list created via .readlines() from file.
    print(line)
file.close()





