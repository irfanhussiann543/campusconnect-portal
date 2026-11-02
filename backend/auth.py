from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.models import AdminUser

auth_bp = Blueprint("auth", __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_id" not in session:
            flash("Please sign in to access the administrator portal.", "warning")
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@auth_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if "admin_id" in session:
        return redirect(url_for("admin.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            flash("Username and password are required.", "danger")
            return render_template("login.html")

        user = AdminUser.query.filter((AdminUser.username == username) | (AdminUser.email == username)).first()
        if user and user.check_password(password):
            session["admin_id"] = user.id
            session["admin_username"] = user.username
            session["admin_name"] = user.full_name
            session["admin_role"] = user.role
            flash(f"Welcome back, {user.full_name}!", "success")
            
            next_url = request.args.get("next")
            return redirect(next_url or url_for("admin.dashboard"))
        else:
            flash("Invalid credentials. Please verify username and password.", "danger")

    return render_template("login.html")


@auth_bp.route("/admin/logout")
def logout():
    session.clear()
    flash("You have been signed out successfully.", "info")
    return redirect(url_for("auth.login"))
