from flask import Blueprint, request, render_template

main = Blueprint("main", __name__)

@main.route("/")
def MainPage():
    return "Hello World"