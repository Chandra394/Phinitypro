#first create database in entry1.py and then go for creating table and inserting values in the file entry2.py

import mysql.connector

# connect to server
db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Cpsingh",
    
)
print(db_connection)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE dbcon1") #new database created.
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)