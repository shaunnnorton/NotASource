from flask import Blueprint, request, render_template

main = Blueprint("main", __name__)

@main.route("/")
def MainPage():
    return render_template("home.html")

@main.route("/wiki")
def WikiPage():
    return render_template("wiki.html")