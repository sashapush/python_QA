# host, database/schema name, user, password #### PythonAutomation/ apidevelop
# conn = mysql.connector.connect(host="localhost", database="apidevelop", user="root", password="root")
from api.BackEndAutomation.utils.configs import getDbConnection

conn = getDbConnection()  # optimised version
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
assert sum == 340
query = "update customerInfo set Location = %s where CourseName = %s;"
data = ("US", "Jmeter")
#or f"update customerInfo set Location = {location} where CourseName = {name};"
cursor.execute(query, data)
conn.commit()  # commits current transaction, used with update
print("Update successful")
cursor.execute(f"delete from customerInfo where courseName = 'WebServices';")
conn.commit()
print("Delete successful")


conn.close()  # close connection to database server
