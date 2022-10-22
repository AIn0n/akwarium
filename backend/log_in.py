from app import app
from flask import make_response, request, redirect, url_for, abort
import flask_login as fl


# login part
login_manager = fl.LoginManager()
login_manager.init_app(app)
logged_users = set()

#user class
class User(fl.UserMixin):
    def __init__(self, name) -> None:
        super().__init__()
        id = name

# TODO: remove!
i = 0
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
        fl.login_user(user)
        return redirect(url_for("hello"))
    return abort(418)

@app.route("/logout")
@fl.login_required
def logout():
    #logout_user()
    return redirect(url_for("login"))#TEMP
