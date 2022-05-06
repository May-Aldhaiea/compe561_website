# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     port="3306",
#     user="root",
#     passwd="",
#     database="flask"
# )
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO flask (email, password) VALUES (%s, %s)"
# val = ("demo@gmail.com", "randompassword")
# mycursor.execute(sql, val)
#
#
# mydb.commit()  # The data table contents are updated and must be used to this statement
#
# print(mycursor.rowcount, "Record insertion succeeded.")

from flask import Flask, render_template, request, flash, url_for, redirect, session
import mysql.connector

selectMovies = 'SELECT * FROM movies'
selectReviews = 'SELECT * FROM reviews'
app = Flask(__name__);
app.secret_key = "super secret key"

@app.route("/signup",  methods=["GET", "POST"])
def signup():
    connection = mysql.connector.connect(host="localhost", port="3306", user="root", database="DATABASENAME")
    cursor = connection.cursor()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        insertSyntax = (
            "INSERT INTO `users` ( `email`, `password`)"
            " VALUES ( %s, %s);"
        )
        insertData = (email, password)
        cursor.execute(insertSyntax, insertData)
        print(cursor.statement)
        cursor.execute('COMMIT;')
        cursor.close()

    return render_template("signup.html");

@app.route("/login", methods=["GET", "POST"])
def login():
    connection = mysql.connector.connect(host="localhost", port="3306", user="root", database="DATABASENAME")
    cursor = connection.cursor()
    user = [session['loggedin'], session['email']]
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE email=%s AND password=%s', (email, password))
        record = cursor.fetchone()
        #print(record)
        if record:
            session['loggedin']= True
            session['email']= record[0]
            return redirect(url_for('home'))
        else:
            print("false")
            return redirect(url_for('signup'))
    return render_template("login.html", user=user);

@app.route("/logout/")
def logout():
    session['username']=''
    session['email']=''
    session['loggedin'] = False
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)