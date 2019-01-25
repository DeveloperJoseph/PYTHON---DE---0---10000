## PYTHON DATETIME ##
# A date in Python is not a data type of its own, 
# but we can import a module named 'datetime' to work 
# with dates as date objects.
#Example:
    # Import the datetime module and display the current
    # date.
import datetime
x = datetime.datetime.now()
print(x)

#Date Output:
#- When we execute the code from the example above the result will be:
# 2019-01-13 20:36:46.574386
#- The date contains year, month, day, hour, minute, second and microsecond.
#- The datetime module has many methos to return information about 
#  the date object.
#- Here are a few examples, you will learn more about them later 
#  in this chapter.
#Example:
    # Return the year and name of weekday:
print(x.year)
print(x.strftime("%A"))

#Creating Date Objects:
#To create a date, we can use the datetime() class (constructor) of the 
#datetime module.
#The datetime() class requires three parameters to create a date: year,month,day.
#Example:
    # Create a date object:

year = int(input(">> Year: "))
month = int(input(">> Month: "))
day = int(input(">> Day: "))

new_date = datetime.datetime(year,month,day)
print("#> Fecha created: ",new_date)

#The datetime() class also takes paremeters for time and
#timezone(hour,minute,second,microsecond,tzone), but they
#are optional, and has a default value of 0,(None for timezone).

#The strftime() Method:
#- The datetime object has a method for formatting date objects into readable
#  strings.
#- The method is called strftime(), and takes one paremeter, format, to specify 
#  the format of the returned string
print("Your birthday is on: ",new_date.strftime("%B"))
print("Your birthday is the day of year: ",new_date.strftime("%j"))




