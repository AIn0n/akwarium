from app import app, users_db, logs_db
from flask import request, jsonify
import flask_login as fl
from bson.objectid import ObjectId
from datetime import datetime


@app.route("/log-newest", methods=["GET"])
@fl.login_required
def log_newest():
    id = fl.current_user.id
    aquarium = request.form["aquarium"]

    x = users_db.find_one({"_id": ObjectId(str(id))})
    x = logs_db.find_one({"_id": x["logs_id"]})
    if x[aquarium][-1] == "":
        return jsonify({"message": "No logs", "code": 418})
    else:
        return jsonify({"message": x[aquarium][-1], "code": 200})


@app.route("/log-all", methods=["GET"])
@fl.login_required
def log_all():
    id = fl.current_user.id
    aquarium = request.form["aquarium"]

    x = users_db.find_one({"_id": ObjectId(str(id))})
    x = logs_db.find_one({"_id": x["logs_id"]})
    if x[aquarium][-1] == "":
        return jsonify({"message": "No logs", "code": 418})
    else:
        return jsonify({"message": x[aquarium], "code": 200})


@app.route("/log-add", methods=["POST"])
@fl.login_required
def log_add():
    id = fl.current_user.id
    aquarium = request.form["aquarium"]
    kh = request.form["kh"]
    gh = request.form["gh"]
    ph = request.form["ph"]
    no2 = request.form["no2"]
    no3 = request.form["no3"]

    obj = {
        "date": datetime.now(),
        "kh": kh,
        "gh": gh,
        "ph": ph,
        "no2": no2,
        "no3": no3,
    }

    x = users_db.find_one({"_id": ObjectId(str(id))})
    logs_db.find_one_and_update(
        {"_id": x["logs_id"]}, {"$push": {aquarium: obj}}
    )
    return "Success", 200
