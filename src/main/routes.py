from crypt import methods
from flask import Blueprint, request, render_template
from src.utils.fetch import get_page, strip_page, get_refrences

main = Blueprint("main", __name__)

@main.route("/")
def MainPage():
    return render_template("home.html")

@main.route("/wiki", methods=["GET","POST"])
def WikiPage():
    data = {
        "body":"<h1>Hello World</h1>"
    }
    link = request.args.get("link")
    response = get_page(link)
    stripped_page = strip_page(response.text)
    data["body"] = stripped_page
    data['source_list'], data["sources"] = get_refrences(stripped_page)
    return render_template("wiki.html",**data)