import os
from flask import Flask, redirect, url_for, render_template, request, Markup
from testLog import *

app = Flask(__name__)

teaching = Markup("""
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/slide1.jpg" alt="tmpImage1">
                <div class="caption">Temp Image 1</div>
            </div>
        </a>
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/slide2.jpg" alt="tmpImage2">
                <div class="caption">Temp Image 2</div>
            </div>
        </a>
        <a href="#">
            <div class="aSlide fade">
                <img src="/static/images/slide3.jpg" alt="tmpImage3">
                <div class="caption">Temp Image 3</div>
            </div>
        </a>
        <div id="floatTeaching">
            teaching<span style="color: red">@CS</span>
        </div>
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