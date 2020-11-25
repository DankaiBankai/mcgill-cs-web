import os
from flask import Flask, redirect, url_for, render_template, request, Markup


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
        <a>
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
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
    return render_template()

if __name__ == "__main__":
    app.run()