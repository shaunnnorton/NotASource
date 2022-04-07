from crypt import methods
from flask import Blueprint, flash, request, render_template, redirect, url_for
from src.utils.fetch import check_if_link, get_page, get_page_no_link, strip_page, get_refrences, test_link

main = Blueprint("main", __name__)

@main.route("/")
def MainPage():
    return render_template("home.html")

@main.route("/wiki", methods=["GET","POST"])
def WikiPage():
    """Route that displays a wikipedia page and all sources on it."""
    data = {
        "body":"<h1>Hello World</h1>"
    }
    link = request.args.get("link")
    if not check_if_link(link):
        link = get_page_no_link(link)
    response = get_page(link)
    test, status = test_link(link)
    if not test:
        flash(f"Error: That query did not lead to a vaild WikiPedia page. Status Code ({status})")
        return render_template("home.html")
    stripped_page = strip_page(response.text)
    data["body"] = stripped_page
    data['source_list'], data["sources"] = get_refrences(stripped_page)
    return render_template("wiki.html",**data)

@main.route("/wiki/<term>")
def WikiRedirect(term):
    """Redirects to WikiPage Route to provide relative link functionality."""
    return redirect(url_for("main.WikiPage",link=term))