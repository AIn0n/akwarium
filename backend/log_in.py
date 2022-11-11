from app import app, users_db
from flask import make_response, request, redirect, url_for, abort
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

# TODO: remove!
i = 0


@app.route("/hello", methods=["GET"])
def hello():
    global i
    i += 1
    return make_response({"hello": "", "counter": i}, 200)


@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    password = request.form["password"]
    x = users_db.find_one({"name": name})
    if password == x["password"]:
        user = User(x["_id"])
        fl.login_user(user)
        logged_users.add(user)
        return redirect(url_for("hello"))
    return abort(418)


@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    name = request.form["name"]
    password = request.form["password"]
    users_db.insert_one({"email": email, "name": name, "password": password, "aquarium":[]})
    x = users_db.find_one({"name": name})
    user = User(x["_id"])
    fl.login_user(user)
    logged_users.add(user)
    return redirect(url_for("hello"))


@app.route("/logout")
@fl.login_required
def logout():
    # logout_user()
    return redirect(url_for("login"))  # TEMP


@app.route("/add_aquarium", methods=["POST", "GET"])
@fl.login_required
def add_aquarium():
    id = fl.current_user.id
    print(id)
    print(type(id))
    height = request.form["height"]
    width = request.form["width"]
    length = request.form["length"]
    heater_power = request.form["heater_power"]
    luminocity = request.form["luminocity"]
    pump_power = request.form["pump_power"]
    filter = request.form["filter"]
    obj = {
        "height": height,
        "width": width,
        "length": length,
        "heater_power": heater_power,
        "luminocity": luminocity,
        "pump_power": pump_power,
        "filter": filter, 
    }
    users_db.find_one_and_update(
        {'_id': ObjectId(str(id))},
        {'$push': {"aquarium" : obj}}
    )
    return redirect(url_for("hello"))
