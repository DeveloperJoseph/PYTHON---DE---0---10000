# PYTHON MySQL CREATE TABLE #

#Creating a Table:
# > To create a table in MySQL, use the "CREATE TABLE" statement.
# > Make sure you define the name of the database when you create the connection
#Example: 'Create a table named (customers)':
import mysql.connector
"""
#Connection to MySQL Database:
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
myQueryCreateTable = myDB.cursor() #create a cursor
myQueryCreateTable.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))") #execute query
"""
#If the above code was executed with no errors, you have now succesfully created a table.

#Check If Table Exists:
#You can check if a table exist by listing all table in your database with the "SHOW TABLE" statement.
#Example: 'Returns a list of your system's databases'.
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="facturacion"
)
showTables = myDB.cursor() #create a query
showTables.execute("SHOW TABLES")
#loop for show  tables of my database
for x in showTables:
    print(x)

"""
state = False
try:
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="mydatabase"
    )
    state = True
    print(">> Successful Connection mydatabase")
    if state == True:
        try:
            queryCreateTable = myDB.cursor()    
            rpta = str(input("You wish create the table Customers (y/n): "))
            if rpta.lower() == 'y':
                queryCreateTable.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")
                print(">> Table 'customers' created successful..")
            elif rpta.lower() == 'n':
                print(">> No executed query to the database.")
        except:
            print(">> Wrong to successful connection..")  
except:
    print(">> Something went wrong in connection with database not exists.")
finally:
    print(">> Thanks You..")
"""



