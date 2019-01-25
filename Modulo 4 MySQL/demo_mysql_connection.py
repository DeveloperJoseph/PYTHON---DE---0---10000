# PYTHON MYSQL ##
#Python can be used in database applications.
#One of the most popular databases is MySQL.

# 'MySQL Database' => 
# > To be able experiment with the code examples in this tutorial, 
# you should have MySQL installed on your computer.
# > You can download a free MySQL database at  https://www.mysql.com/downloads/.

# Install MySQL Driver =>
# > Python needs a MySQL driver to acces the MySQL database.
# > In this tutorial we will use the driver "MySQL Connector".
# > We recommend that you use PIP to install "MySQL Connector"
# > Pip is most likely already installed in yout Python environment.
# > Navigate your command line to the location of PIP, and type the following: 
                                                            #  'pip install mysql-connector'

# Test MySQL Connector: To test if tge installation was successful, or if you already have
#                        "MySQL Connector" installed, create a Python page with the following
#                         content.
# Note: If the above was executed with no errors, "MySQL Connector" is installed and ready to
# be used.


# CREATE CONNECTION:
# Start by creating a connection to the database.
# Use the username and password from your MySQL Database:     
import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)
print(myDB)
#Now you can start querying the databse using 
#SQL statements.