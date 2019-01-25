#PYTHON MySQL CREATE DATABASE:

#Creating a DataBase:
#To create a database in MySQL, use the "CREATE DATABASE" statement.
#Example: 'Create a database named 'mydatabase'

import mysql.connector

# Established connection
""""
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)
"""
#If the above code was executed with no errors, you have succesfully created database
"""
#Created a database
queryCreateDatabase = myDB.cursor()
queryCreateDatabase.execute("CREATE DATABASE mydatabase")
print(">> Succesfully Created Database.")
"""

#Check if Database Exists:
#You can check if a database exist by listing all databases in your system by using the
#'SHOW DATABASES' statement.
#Example:
# Returns a list of your system's databases:
"""
myQuery = myDB.cursor()
myQuery.execute("SHOW DATABASES")
for x in myQuery:
    print(x)
"""
#Or you can try to access the database when making the connection:
#Example: 'Try connecting to the database 'mydatabase'
"""
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
"""
#If the database does not exit, you will get an error.

