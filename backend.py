#!/usr/bin/python3
import pymysql
import os
from flask import Flask, redirect, url_for, render_template, request, Markup, make_response
import SQL_Interface
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

#GET home page
@app.route("/", methods=["GET"])
def home():
    query_string = "SELECT content FROM teaching"
    data = SQL_Interface.query(query_string)
    teaching = data[0][0]
    editTeaching = Markup("""<a id="edit" href="/editTeaching" style="text-decoration: none; color: white"><span style="color: red">Edit Teaching</span></a>""")
    return render_template("index.html", teaching=teaching, editTeaching=editTeaching)

#GET edit page or POST user edits
@app.route("/editTeaching", methods=["POST", "GET"])
def editTeaching():
    if request.method == "POST":
        newteaching = request.form["editArea"]
        # add to database
        teaching = Markup(newteaching)
        print(teaching)
        teaching = SQL_Interface.format_to_sql(teaching)
        update_string =  """UPDATE teaching SET content='{0}' WHERE ID=0"""
        update_string = update_string.format(teaching)
        SQL_Interface.update(update_string)
        print("teaching content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM teaching"
        data = SQL_Interface.query(query_string)
        teaching = data[0][0]
        teaching = SQL_Interface.format_to_user(teaching)
        return render_template("html/edit/editTeaching.html", teaching=teaching) #Just like render() in NodeJS or Django

#GET login page
@app.route("/login", methods=["GET"])
def login():
    return render_template("html/login/login.html")

#POST user credentials to attemp login
@app.route("/attempt-login", methods=["POST", "GET"])
def attempt_login():
    data = request.get_json()
    username = data['credentials']['username']
    password = data['credentials']['password']
    logged_in = SQL_Interface.checkCredentials(username, password)

    if logged_in:
        ticket = SQL_Interface.generateTicket(username)
        return json.dumps({"message": "Success", "ticket": ticket})
    else:
        return json.dumps({"message": "Wrong username or password"})

#GET prospective-menu page
@app.route('/prospective', methods=["GET"])
def prospective():
    return render_template("html/prospective/menu-prospective.html")

#GET general info page
@app.route('/general_info', methods=["GET"])
def gen_info():
    query_string = "SELECT content FROM prospective WHERE ID='generalInfo'"
    data = SQL_Interface.query(query_string)
    content = data[0][0]
    editGenInfo = Markup("""<a id="edit" href="/editGeneralInfo" style="text-decoration: none;"><span>Edit</span></a>""")
    return render_template("html/prospective/gen-info.html", edit=editGenInfo, content=content)

#GET edit page or POST user edits
@app.route('/editGeneralInfo', methods=["POST", "GET"])
def edit_gen_info():
    if request.method == "POST": #Retrieve user edits and commit to DB
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective SET content='{0}' WHERE ID='generalInfo'"""
        update_string = update_string.format(newInfo)
        SQL_Interface.update(update_string)
        print("general info content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else: #Retrieve edit page with prefilled edit box
        query_string = "SELECT content FROM prospective WHERE ID='generalInfo'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editGeneralInfo.html", content=info)

#GET whyCS page
@app.route('/why', methods=["GET"])
def why_cs():
        query_string = "SELECT content FROM prospective WHERE ID='whyCS'"
        data = SQL_Interface.query(query_string)
        content = data[0][0]
        editWhyCS = Markup("""<a id="edit" href="/editWhyCS" style="text-decoration: none;"><span>Edit</span></a>""")
        return render_template("html/prospective/why.html", edit=editWhyCS, content=content)

#GET edit page or POST user edits
@app.route('/editWhyCS', methods=["POST", "GET"])
def edit_whyCS():
    if request.method == "POST": #Retrieve user edits and commit to DB
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective SET content='{0}' WHERE ID='whyCS'"""
        update_string = update_string.format(newInfo)
        SQL_Interface.update(update_string)
        print("why CS content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:#Retrieve edit page with prefilled edit box
        query_string = "SELECT content FROM prospective WHERE ID='whyCS'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editWhyCS.html", content=info)

#GET Undergrads page
@app.route('/undergrads', methods=["GET"])
def undergrads():
    query_string = "SELECT content FROM prospective WHERE ID='undergrads'"
    data = SQL_Interface.query(query_string)
    content = data[0][0]
    editUndergrads = Markup("""<a id="edit" href="/editUndergrads" style="text-decoration: none;"><span>Edit</span></a>""")
    return render_template("html/prospective/undergrads.html", edit=editUndergrads, content=content)

#GET edit page or POST user edits
@app.route('/editUndergrads', methods=["POST", "GET"])
def edit_undergrads():
    if request.method == "POST":#Retrieve user edits and commit to DB
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective SET content='{0}' WHERE ID='undergrads'"""
        update_string = update_string.format(newInfo)
        SQL_Interface.update(update_string);
        print("undergrads content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:#Retrieve edit page with prefilled edit box
        query_string = "SELECT content FROM prospective WHERE ID='undergrads'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editUndergrads.html", content=info)

#GET people menu page
@app.route('/people-menu', methods=["GET"])
def people():
    return render_template("html/people/menu-people.html")

#GET academic menu page
@app.route('/academic-menu', methods=["GET"])
def academic():
    return render_template("html/academic/menu-academic.html")

#GET news page
@app.route('/news', methods=["GET"])
def news():
    return render_template("html/news/news.html")

#GET about menu page
@app.route('/about-menu', methods=["GET"])
def about():
    return render_template("html/about/menu-about.html")

#GET research page
@app.route('/research', methods=["GET"])
def research():
    return render_template("html/research/research.html")

#POST value of sotred ticket cookie and check if value matches DB
@app.route('/verify-ticket', methods=["POST", "GET"])
def verifyTicket():
    data = request.get_json()
    ticket = data['verify']['ticket']
    message = SQL_Interface.verify(ticket)
    return json.dumps({"message": message})


if __name__ == "__main__":
    app.run()
