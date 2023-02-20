# a = 1
# while a <= 4:
#    b = a * 2
#    a = a + 2
#    print(b)

# if __name__ == '__main__':
#     n = int(input())
#     for item in range(0, n):
#         print(item * item)

# filter() returns object(iterator) where items are filtered through a function to test if the item is accepted or not
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x)


def myfunc(a):
    return len(a)


tu = ('apple', 'banana', 'cherry')
x = map(myfunc, (tu))

print(x)

# convert the map into a list, for readability:
print(list(x))

print(1 == '1')

print(True * 2)
