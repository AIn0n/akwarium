from app import app, users_db
from flask import request, abort
import flask_login as fl
from bson.objectid import ObjectId

# login part
login_manager = fl.LoginManager()
login_manager.init_app(app)
logged_users = set()

# user class
class User(fl.UserMixin):
    def __init__(self, name) -> None:
        super().__init__()
        self.id = name


@login_manager.user_loader
def load_user(id):
    id = ObjectId(str(id))
    for user in logged_users:
        if user.id == id:
            return user
    return None


@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    password = request.form["password"]
    x = users_db.find_one({"name": name})
    if password == x["password"]:
        user = User(x["_id"])
        fl.login_user(user)
        logged_users.add(user)
        return "Success", 200
    return abort(418)


@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    name = request.form["name"]
    password = request.form["password"]
    users_db.insert_one(
        {"email": email, "name": name, "password": password, "aquarium": []}
    )
    x = users_db.find_one({"name": name})
    user = User(x["_id"])
    fl.login_user(user)
    logged_users.add(user)
    return "Success", 200


@app.route("/logout")
@fl.login_required
def logout():
    logged_users.remove(fl.current_user)
    fl.logout_user()
    return "Success", 200