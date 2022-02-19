from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
# @login_required  # ----> Activate when page is only to be viewed when logged in.
def home():
    return render_template("home.html", user=current_user)


@views.route("/secret")
@login_required  # ----> Activate when page is only to be viewed when logged in.
def secret():
    return render_template("secret.html", user=current_user)
