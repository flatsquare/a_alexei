from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__,template_folder="../html" )

ID_IND = 0
ID_CORP = 0
ID_NOM = 0

@app.route("/individualDatalog", methods=['POST'])
def individual_client_data_get():
    global ID_IND
    ID_IND += 1
    id = ID_IND
    email = request.form['email']
    password = request.form['password']

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu!NNel0024jenxoksi",
        database="lobusch_users_data"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO log_users_data_individual (id_num, email, password) VALUE (%s, %s, %s)"
    val = (id, email, password)
    mycursor.execute(sql, val)

    mydb.commit()
    return render_template('individualFlowHTML/individualData.html')
# ---------------------------------next form

@app.route("/id_client_data", methods=['POST'])
def id_individual_client_company_data_get():
    global ID_IND
    ID_IND += 1
    id = ID_IND
    company_name = request.form['company_name']
    company_activities = request.form['company_activities']
    capital = request.form['capital']
    restrictions = request.form['restrictions']
    first_name = request.form['first_name']
    family_name = request.form['surname']
    birthdate = request.form['birthdate']
    place_of_birth = request.form['place_of_birth']
    phone_number = request.form['phone_number']
    citizen_of = request.form['citizen_of']
    passport_number = request.form['passport']
    issuing_authority = request.form['issuing_authority']
    date_of_expiry = request.form['date_of_expiry']




    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu!NNel0024jenxoksi",
        database="lobusch_users_data"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO individual_users_id_data ( id_num, company_name, company_activities, charter_capital, director_restriction, first_name, family_name, birth_date, place_of_birth, phone_number, citizen_of, passport_number, issuing_authority, date_of_expiery) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
    val = (id, company_name, company_activities, capital, restrictions, first_name, family_name, birthdate, place_of_birth, phone_number, citizen_of, passport_number, issuing_authority, date_of_expiry)
    mycursor.execute(sql, val)

    mydb.commit()
    return render_template('IndividualFlowHTML/email_form.html')


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
    app.run(debug=True)
