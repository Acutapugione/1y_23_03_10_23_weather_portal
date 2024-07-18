from flask import render_template

from .. import app


@app.get("/")
def index():
    # print(app.config)
    # exit()
    return render_template("index.html")


@app.get("/about")
def about():
    return "about"
