#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="Cpsingh",  # your password
                     db="dblogin")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM user_login")

# print all the first cell of all the rows
for row in cur.fetchall():
    print (row[0])
    print(row[1])
    print("task accomplished")

db.close()