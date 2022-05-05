import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    database="flask"
)
mycursor = mydb.cursor()

sql = "INSERT INTO flask (email, password) VALUES (%s, %s)"
val = ("demo@gmail.com", "randompassword")
mycursor.execute(sql, val)


mydb.commit()  # The data table contents are updated and must be used to this statement

print(mycursor.rowcount, "Record insertion succeeded.")
