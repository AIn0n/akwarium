from app import app, users_db
from flask import request
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
    current_password = request.form["current_password"]

    # Password validation
    db_current_user = users_db.find_one({"_id": ObjectId(str(id))})
    if current_password != db_current_user["password"]:
        return "Incorrect current password."

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
