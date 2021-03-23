#execute this file only first executing entry1.py(note:you need to execute/run entry1.py file only once for creating database)

import mysql.connector

# connect to server
db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Cpsingh",
    db="dbcon1" #database just created in entry1.py
)

# get a cursor
db_cursor = db_connection.cursor()

# delete if the table exists
db_cursor.execute("DROP TABLE IF EXISTS user")

sql = """CREATE TABLE user (
         id INT AUTO_INCREMENT PRIMARY KEY,
    
         firstname  CHAR(50),
         lastname  CHAR(50),
         username varchar(60),
         urpassword varchar(100),
         phno int(15),
         email varchar(60)

         )"""

# execute a query
db_cursor.execute(sql)

sql_insert = "INSERT INTO user(firstname,lastname,username,urpassword,phno,email) VALUES('cp','singh','cpsingh','cpsingh1234',1234567891,'cp@gmail.com')"

#Execute cursor and pass query 

db_cursor.execute(sql_insert)
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted you can check in your mysql database")

# close the connection
db_connection.close()

# If the above code is executed with no error, we have successfully created primary key.
