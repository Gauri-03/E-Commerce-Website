from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from hci.models import User, Product, Category
import json

auth = Blueprint("auth", __name__)

@auth.route("/", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        form_username  = request.form.get("username")
        form_password = request.form.get("password")
        user = User.query.filter_by(username = form_username).first()
        if user:
            if User.query.filter_by(password = form_password).first():
                return redirect(url_for("user.userdashboard",user_id = user.id))
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")
    return render_template("login.html")