# PYTHON MYSQL INSERT INTO TABLE #

# INSERT INTO TABLE:
# To fill a table in MySQL, use the "INSERT INTO" statement.
#Example:
# Insert a record in the "customers" table.
import mysql.connector

try:
    myDB = mysql.connector.connect(
        host =  "localhost",
        user = "root",
        passwd = "root",
        database = "mydatabased"
    )
except:
    print("> Error en connection with the database")

try:
    queryInsertInto = myDB.cursor()
    print("> Creating a insert query sql..")
    sql =  "INSERT INTO customers(name,address) VALUES ('{}','{}')".format("Daniel","Street Smith 18")
    queryInsertInto.execute(sql)
    myDB.commit()
    print(queryInsertInto.rowcount, "records inserted.")
    showTable = myDB.cursor()
    print("> Creating a select query sql..")
    sql = "SELECT * FROM customers" 
    showTable.execute(sql)
    print("> List: ")
    myResult = showTable.fetchall()
    for x in myResult:
        print(x)
except:
    print("> Wrong on code..")

#Important!: Notice the statement => myDB.commit().It is required to make the changes,
#otherwise no changes are made to the table.

#Insert Multiple Rows:




"""
showTable = myDB.cursor()
sql = "SELECT * FROM customers" 
showTable.execute(sql)
myResult = showTable.fetchall()
for x in myResult:
    print(x)
"""