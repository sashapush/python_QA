itemsInCart = 0

if itemsInCart !=2:
    pass
    #raise Exception("not enough products in cart")

assert(itemsInCart == 0)

#try catch
try:
    with open("blank.txt", "r") as file:
        print(file.read())

#basic exception printed as non-basic
except Exception as e:
    print(e)

#custom exception
#except:
#    print("File not found,lol")
finally:
    print("cleaning up the moss")
