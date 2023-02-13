import mysql.connector

# host, database/schema name, user, password #### PythonAutomation/ apidevelop
conn = mysql.connector.connect(host="localhost", database="apidevelop", user="root", password="root")
print(conn.is_connected())  # checking if connection is successfully established

cursor = conn.cursor()  # creating a stream between python and database
cursor.execute("SELECT c. * from customerinfo c ORDER BY c.Amount desc;")  # now we can execute query
# row = cursor.fetchone() #.fetchone returns first row as #tuple
# print(row)
table = cursor.fetchall()  # returns the rest, doesn't return duplicate row from .fetchone(first row)
print(table)  # list of tuples
print(table[0][3])
sum = 0
for item in table:
    sum += item[2]
print(sum)
