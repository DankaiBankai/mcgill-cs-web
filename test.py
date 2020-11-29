import os
from flask import Flask, redirect, url_for, render_template, request, Markup
from testLog import *

app = Flask(__name__)

teaching = Markup("""
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/29_Remote_Learning_Resources...._Xj4iyVJ.png" alt="tmpImage1">
                <div class="caption">Remote Learning Resources</div>
            </div>
        </a>
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/24_Remote_Teaching_in_the_Fall.png" alt="tmpImage2">
                <div class="caption">Remote Teaching in The Fall</div>
            </div>
        </a>
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/StudentInLectureHallWearingMask-767x431.png" alt="tmpImage3">
                <div class="caption">Current state of Covid-19</div>
            </div>
        </a>
    """)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", teaching=teaching)

@app.route("/login", methods=["POST", "GET"])
def login():
    print("/login")
    return render_template("html/login/login.html")

@app.route("/attempt-login", methods=["POST", "GET"])
def attempt_login():
    print("/attemp-login")
    if request.method == "POST":
        testLog()
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
    return render_template("html/news/news.html")

@app.route('/about-menu')
def about():
    return render_template("html/about/menu-about.html")
@app.route('/research')
def research():
    return render_template("html/research/research.html")


if __name__ == "__main__":
    app.run()