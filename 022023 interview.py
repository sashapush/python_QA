print(1 == (1))
print("1" == True)
print(0.1 + 0.2 == 0.3)
print(2 * False + True == True)
print(max("String"))
print(type(max("String")))  #
print(False == "")
print(2 == (2,))
print(None == "")
print(type((1)))

a = range(1, 7)
b = {i for i in range(1, 7)}
print(list(filter(lambda el: el == 5, b)))  # [5]
print(list(map(lambda el: el * -1, a)))  # [-1, -2, -3, -4, -5, -6]

print(type(2, ))

print(1 == (1))  # True
print("1" == True)  # false
print(0.1 + 0.2 == 0.3)  # False, it's = 0.30000000000000004
print(2 * False + True == True)  # True (2*0 + 1 = 1)
print(max("String"))  # t has the biggest position in alphabet - hence t is returned
print(type(max("String")))  # string
print(False == "")  # False; False = 0
print(2 == (2,))  # False
print(None == "")  # False
print(type((1)))  # integer