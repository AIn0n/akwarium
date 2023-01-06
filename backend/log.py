from app import app, users_db, logs_db, species_db
from flask import request, jsonify
import flask_login as fl
from bson.objectid import ObjectId
from datetime import datetime


@app.route("/log-newest/<aquarium>", methods=["GET"])
@fl.login_required
def log_newest(aquarium=None):
    id = fl.current_user.id

    x = users_db.find_one({"_id": ObjectId(str(id))})
    x = logs_db.find_one({"_id": x["logs_id"]})
    if x[aquarium][-1] == "":
        return jsonify({"message": "No logs", "code": 418})
    else:
        return jsonify({"message": x[aquarium][-1], "code": 200})


@app.route("/log-all/<aquarium>", methods=["GET"])
@fl.login_required
def log_all(aquarium=None):
    id = fl.current_user.id

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
        "KH": kh,
        "GH": gh,
        "pH": ph,
        "NO2": no2,
        "NO3": no3,
    }

    x = users_db.find_one({"_id": ObjectId(str(id))})
    logs_db.find_one_and_update(
        {"_id": x["logs_id"]}, {"$push": {aquarium: obj}}
    )
    return "Success", 200


def water_update(id, aquarium):
    x = users_db.find_one({"_id": ObjectId(str(id))})
    for aq in x["aquarium"]:
        if aq["name"] == aquarium:
            x = aq

    min = {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""}
    max = {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""}

    for fish in x["fish"]:
        species = species_db.find_one({"name": fish["species"]})
        for el in ["KH", "GH", "pH", "NO2", "NO3"]:
            if species["water_requirements"]["min"][el] != "":
                if min[el] == "" or float(min[el]) < float(
                    species["water_requirements"]["min"][el]
                ):
                    min[el] = float(species["water_requirements"]["min"][el])
            if species["water_requirements"]["max"][el] != "":
                if max[el] == "" or float(max[el]) > float(
                    species["water_requirements"]["max"][el]
                ):
                    max[el] = float(species["water_requirements"]["max"][el])

    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))},
        {
            "$set": {
                "aquarium.$[a].water_max.0": max,
                "aquarium.$[a].water_min.0": min,
            }
        },
        array_filters=[{"a.name": aquarium}],
    )
