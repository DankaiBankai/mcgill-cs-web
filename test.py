#!/usr/bin/python3
import pymysql
import os
from flask import Flask, redirect, url_for, render_template, request, Markup, make_response
import SQL_Interface
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# pass usualTeaching if user doesn't have permission and editTeaching2 if he does
usualTeaching = Markup("""teaching<span style="color: red">@CS</span>""")
editTeaching2 = Markup("""<a id="edit" href="/editTeaching" style="text-decoration: none; color: white"><span style="color: red">Edit Teaching</span></a>""")

@app.route("/", methods=["GET"])
def home():
    query_string = "SELECT content FROM teaching"
    data = SQL_Interface.query(query_string)
    teaching = data[0][0]
    #check if have permission, change usualTeaching to editTeaching
    return render_template("index.html", teaching=teaching, editTeaching=editTeaching2)

@app.route("/editTeaching", methods=["POST", "GET"])
def editTeaching():
    if request.method == "POST":
        newteaching = request.form["editArea"]
        # add to database
        teaching = Markup(newteaching)
        teaching = SQL_Interface.format_to_sql(teaching)
        update_string =  """UPDATE teaching
                            SET content='{0}'
                            WHERE ID=0"""
        update_string = update_string.format(teaching)
        print("teaching content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM teaching"
        data = SQL_Interface.query(query_string)
        teaching = data[0][0]
        teaching = SQL_Interface.format_to_user(teaching)
        return render_template("html/edit/editTeaching.html", teaching=teaching)

@app.route("/login", methods=["POST", "GET"])
def login():
    print("/login")
    return render_template("html/login/login.html")

@app.route("/attempt-login", methods=["POST", "GET"])
def attempt_login():
    print("/attemp-login")
    data = request.get_json()
    print(data)
    username = data['credentials']['username']
    password = data['credentials']['password']
    logged_in = SQL_Interface.checkCredentials(username, password)
    if logged_in:
        print("loggged in")
        ticket = SQL_Interface.generateTicket(username)
        return json.dumps({"message": "Success", "ticket": ticket})
    else:
        return json.dumps({"message": "Wrong username or password"})

@app.route('/prospective')
def prospective():
    return render_template("html/prospective/menu-prospective.html")

@app.route('/general_info')
def gen_info():
    query_string = "SELECT content FROM prospective WHERE ID='generalInfo'"
    data = SQL_Interface.query(query_string)
    content = data[0][0]
    editGenInfo = Markup("""<a id="edit" href="/editGeneralInfo" style="text-decoration: none;"><span>Edit</span></a>""")
    return render_template("html/prospective/gen-info.html", edit=editGenInfo, content=content)

@app.route('/editGeneralInfo', methods=["POST", "GET"])
def edit_gen_info():
    if request.method == "POST":
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective
                        SET content={0}
                        WHERE ID='generalInfo'"""
        update_string = update_string.format(newInfo)
        print("general info content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM prospective WHERE ID='generalInfo'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editGeneralInfo.html", content=info)

@app.route('/why')
def why_cs():
        query_string = "SELECT content FROM prospective WHERE ID='whyCS'"
        data = SQL_Interface.query(query_string)
        content = data[0][0]
        editWhyCS = Markup("""<a id="edit" href="/editWhyCS" style="text-decoration: none;"><span>Edit</span></a>""")
        return render_template("html/prospective/why.html", edit=editWhyCS, content=content)

@app.route('/editWhyCS', methods=["POST", "GET"])
def edit_whyCS():
    if request.method == "POST":
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective
                          SET content={0}
                          WHERE ID='generalInfo'"""
        update_string = update_string.format(newInfo)
        print("why CS content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM prospective WHERE ID='whyCS'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editWhyCS.html", content=info)

@app.route('/undergrads')
def undergrads():
    query_string = "SELECT content FROM prospective WHERE ID='undergrads'"
    data = SQL_Interface.query(query_string)
    content = data[0][0]
    editUndergrads = Markup("""<a id="edit" href="/editUndergrads" style="text-decoration: none;"><span>Edit</span></a>""")
    return render_template("html/prospective/undergrads.html", edit=editUndergrads, content=content)

@app.route('/editUndergrads', methods=["POST", "GET"])
def edit_undergrads():
    if request.method == "POST":
        newInfo = request.form["editArea"]
        newInfo = SQL_Interface.format_to_sql(newInfo)
        update_string ="""UPDATE prospective
                          SET content={0}
                          WHERE ID='undergrads'"""
        update_string = update_string.format(newInfo)
        print("undergrads content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM prospective WHERE ID='undergrads'"
        data = SQL_Interface.query(query_string)
        info = data[0][0]
        info = SQL_Interface.format_to_user(info)
        return render_template("html/edit/editUndergrads.html", content=info)

@app.route('/people-menu')
def people():
    return render_template("html/people/menu-people.html")

@app.route('/academic-menu')
def academic():
    return render_template("html/academic/menu-academic.html")

@app.route('/news')
def news():
    return render_template("html/news/news.html")

@app.route('/about-menu')
def about():
    return render_template("html/about/menu-about.html")

@app.route('/research')
def research():
    return render_template("html/research/research.html")

@app.route('/verify-ticket', methods=["POST", "GET"])
def verifyTicket():
    data = request.get_json()
    print(data)
    ticket = data['verify']['ticket']
    message = SQL_Interface.verify(ticket)
    return json.dumps({"message": message})

if __name__ == "__main__":
    app.run()
