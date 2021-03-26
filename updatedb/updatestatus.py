import mysql.connector
#def state():
status = int(input("Enter the id:"))
update = input("enter new value:")
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Cpsingh", database="dbcon1")
cur = myconn.cursor()
sqlFormula = "UPDATE status SET status=%s WHERE id = %s"
cur.execute(sqlFormula,(update,status))
print("updated sucessfully")
myconn.commit()




