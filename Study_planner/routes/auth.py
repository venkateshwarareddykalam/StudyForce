from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from firebase_setup import auth

auth_bp = Blueprint("auth", __name__)

# Signup Route
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.form
    email = data.get("email")
    password = data.get("password")

    try:
        user = auth.create_user(email=email, password=password)
        return redirect(url_for("dashboard"))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Login Page
@auth_bp.route("/login")
def login_page():
    return render_template("index.html")
