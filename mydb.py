import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    )

# prepare cursor object
cursorObject = dataBase.cursor()

# create the database
cursorObject.execute("CREATE DATABASE elderco")

print("all done!!")
