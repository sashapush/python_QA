import csv

with open("utils\\loan_data_bdd.csv", "r") as csvFile:
    Obj = csv.reader(csvFile, delimiter=",")
    # print(Obj)# reader object
    # print(list(Obj))
    names = []
    amounts = []
    status = []

    for row in Obj:  # Obj is iterable
        # rint(row)

        names.append(row[0])
        amounts.append(row[1])
        status.append(row[2])
# print(names)
# print(amounts)
# print(status)
ind = names.index("Vasya")
print(f"{names[ind]} have applied for {amounts[ind]} PLN and got a '{status[ind]}' decision")
