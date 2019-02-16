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
"""
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
#Primary Key:
# > When creating a table, you should also create a column with a unique key
#   for each record.
# > This can be done by defining a PRIMARY KEY.
# > We use the statement "INT AUTO_INCREMENT PRIMARY KEY" wich will insert a 
#   unique key for each record. Starting at 1, and increased by one for each
#   record.
#Example: 'Create primary key when creating the table"
"""
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
myQuery = myDB.cursor()
try:
    myQuery.execute("CREATE TABLE customers(idCustomer INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    print(">> Table Created Customers..")
    try:
        showTables = myDB.cursor()
        showTables.execute("SHOW TABLES")
        print(">> Show tables in {}:")
        for t in showTables:
            print(t)

    except:
        print(">> Wrong in show tables")
except:
    print(">> Connection error or your query")
"""

#If the table already exists, use the ALTER TABLE keyword:
#Example:
#           Create primary key on an existing table:
"""
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)

queryAlterTable = myDB.cursor()
queryAlterTable.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""


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



