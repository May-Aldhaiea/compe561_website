import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="flask"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (email, password) VALUES (%s, %s)"
val = ("flask", "http://localhost/")
mycursor.execute(sql, val)

mydb.commit()  # The data table contents are updated and must be used to this statement

print(mycursor.rowcount, "Record insertion succeeded.")
