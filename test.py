#!/usr/bin/python3
import pymysql
import os
from flask import Flask, redirect, url_for, render_template, request, Markup
import SQL_Interface

app = Flask(__name__)

# Open database connection
db = pymysql.connect("localhost","cs307-group07","q6m527HgKJuLStZD","cs307-group07-DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Query content of 'teaching' slide show in DB
cursor.execute("SELECT content FROM teaching")
rows = cursor.fetchall()
teaching = Markup(rows[0])


@app.route("/", methods=["GET"])
def home():
    query_string = "SELECT content FROM teaching"
    data = SQL_Interface.query(query_string)
    teaching = data[0]
    return render_template("index.html", teaching=teaching)

@app.route("/login", methods=["POST", "GET"])
def login():
    print("/login")
    return render_template("html/login/login.html")

@app.route("/attempt-login", methods=["POST", "GET"])
def attempt_login():
    print("/attemp-login")
    #if request.method == "POST":
        #testLog()
    return render_template("html/login/login.html")

@app.route('/prospective-menu')
def prospective():
    return render_template("html/prospective/menu-prospective.html")

@app.route('/people-menu')
def people():
    return render_template("html/people/menu-people.html")

@app.route('/academic-menu')
def academic():
    return render_template("html/academic/menu-academic.html")

@app.route('/news')
def news():
    teaching = Markup("<h1>HELLOOOOOOOOOO</h1>")
    update_string = """UPDATE teaching
    SET content='{0}'
    WHERE ID=0"""
    update_string = update_string.format(teaching)
    SQL_Interface.update(update_string)
    return render_template("html/news/news.html")

@app.route('/about-menu')
def about():
    return render_template("html/about/menu-about.html")
@app.route('/research')
def research():
    return render_template("html/research/research.html")


if __name__ == "__main__":
    app.run()