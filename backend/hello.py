from app import app
from flask import make_response, request, redirect, url_for, abort
from flask_login import LoginManager, login_user, UserMixin, login_required

login_manager = LoginManager()
login_manager.init_app(app)
i = 0


class User(UserMixin):
    id = "123"


@app.route("/hello", methods=["GET"])
def hello():
    global i
    i += 1
    return make_response({"hello": "", "counter": i}, 200)


def user_login(name, password):
    if password == "qwerty":
        return True
    return False


@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    password = request.form["password"]
    user = User()
    if user_login(name, password):
        login_user(user)
        return redirect(url_for("hello"))
    return abort(418)

@app.route("/logout")
@login_required
def logout():
    #logout_user()
    return redirect(url_for("login"))#TEMP
