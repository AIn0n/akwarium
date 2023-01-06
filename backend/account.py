from app import app, users_db
from flask import request, jsonify
import flask_login as fl
from bson.objectid import ObjectId
import re  # regex


# user class
class User(fl.UserMixin):
    def __init__(self, name) -> None:
        super().__init__()
        self.id = name


@app.route("/change-email", methods=["POST"])
@fl.login_required
def change_email():
    id = fl.current_user.id
    new_email = request.form["new_email"]

    filter = {"_id": ObjectId(str(id))}
    update = {"$set": {"email": new_email}}
    users_db.update_one(filter, update)
    return "Success", 200


@app.route("/change-password", methods=["POST"])
@fl.login_required
def change_password():
    id = fl.current_user.id
    new_password = request.form["new_password"]
    if len(new_password.strip()) == 0:
        return ("Password has no non-whitespace symbols",)

    filter = {"_id": ObjectId(str(id))}
    update = {"$set": {"password": new_password}}
    users_db.update_one(filter, update)
    return "Success", 200


@app.route("/change-username", methods=["POST"])
@fl.login_required
def change_username():
    id = fl.current_user.id
    new_username = request.form["new_username"]

    filter = {"_id": ObjectId(str(id))}
    update = {"$set": {"username": new_username}}
    users_db.update_one(filter, update)
    return "Success", 200


@app.route("/if-admin", methods=["GET"])
@fl.login_required
def admin():
    id = fl.current_user.id
    x = users_db.find_one({"_id": ObjectId(str(id))})
    val = x["admin"]

    return jsonify({"message": val, "code": 200})
