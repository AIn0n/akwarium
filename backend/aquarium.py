from app import app, users_db, device_db, logs_db
from flask import request, jsonify
import flask_login as fl
from bson.objectid import ObjectId
import json


@app.route("/add-aquarium", methods=["POST"])
@fl.login_required
def add_aquarium():
    id = fl.current_user.id
    name = request.form["name"]
    image = request.form["image"]
    height = request.form["height"]
    width = request.form["width"]
    length = request.form["length"]
    heater_id = request.form["heater_id"]
    lamp_id = request.form["lamp_id"]
    pump_id = request.form["pump_id"]
    filter_id = request.form["filter_id"]

    x = users_db.find_one({"_id": id})["aquarium"]
    for el in x:
        if el["name"] == name:
            return jsonify(
                {"message": "This name is already in use", "code": 418}
            )

    if int(height) <= 0:
        return jsonify({"message": "Height too small", "code": 418})
    if int(width) <= 0:
        return jsonify({"message": "Width too small", "code": 418})
    if int(length) <= 0:
        return jsonify({"message": "Length too small", "code": 418})
    try:
        if device_db.find_one({"_id": ObjectId(heater_id)}) == None:
            return jsonify(
                {"message": "This id is incorrect (heater)", "code": 418}
            )
        if device_db.find_one({"_id": ObjectId(lamp_id)}) == None:
            return jsonify(
                {"message": "This id is incorrect (lamp)", "code": 418}
            )
        if device_db.find_one({"_id": ObjectId(pump_id)}) == None:
            return jsonify(
                {"message": "This id is incorrect (pump)", "code": 418}
            )
        if device_db.find_one({"_id": ObjectId(filter_id)}) == None:
            return jsonify(
                {"message": "This id is incorrect (filter)", "code": 418}
            )
    except:
        return jsonify({"message": "Value error", "code": 418})

    obj = {
        "name": name,
        "height": height,
        "width": width,
        "length": length,
        "image": image,
        "heater_id": heater_id,
        "lamp_id": lamp_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "water_min": {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""},
        "water_max": {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""},
        "fish": [],
    }
    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))}, {"$push": {"aquarium": obj}}
    )
    x = users_db.find_one({"_id": ObjectId(str(id))})["logs_id"]
    logs_db.find_one_and_update(
        {"_id": x},
        {"$push": {name: {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""}}},
    )
    return "Success", 200


@app.route("/import-aquarium", methods=["POST"])
@fl.login_required
def import_aquarium():
    # Get current user
    id = fl.current_user.id
    user = users_db.find_one({"_id": ObjectId(str(id))})
    # Request the aquarium object in the form of a json string
    json_string = request.form["json_string"]
    # Decode the string
    aquarium_obj = json.loads(json_string)

    # Check for duplicate name
    names = [aq["name"] for aq in user["aquarium"]]
    if aquarium_obj["name"] in names:
        return "Duplicate name", 419

    # Insert the new aquarium into the database
    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))}, {"$push": {"aquarium": aquarium_obj}}
    )

    x = user["logs_id"]
    logs_db.find_one_and_update(
        {"_id": x},
        {"$push": {aquarium_obj["name"]: {"KH": "", "GH": "", "pH": "", "NO2": "", "NO3": ""}}},
    )
    return "Success", 200


@app.route("/aquariums-names", methods=["GET"])
@fl.login_required
def aquarium_names():
    id = fl.current_user.id
    x = users_db.find_one({"_id": ObjectId(str(id))})
    ret = []
    for aq in x["aquarium"]:
        ret.append({"name": aq["name"], "image": aq["image"]})
    return ret


@app.route("/aquarium/<name>", methods=["GET"])
@fl.login_required
def aquarium_specific(name=None):
    id = fl.current_user.id
    x = users_db.find_one({"_id": ObjectId(str(id))})

    for aq in x["aquarium"]:
        if aq["name"] == name:
            return aq
    return jsonify({"message": "Incorrect name", "code": 418})


@app.route("/devices", methods=["GET"])
@fl.login_required
def device():
    types = ["filter", "light", "pump", "heater"]
    res = {}
    for type in types:
        res[type] = []
        x = device_db.find({"type": type})
        for el in x:
            el["_id"] = str(el["_id"])
            res[type].append(el)
    return jsonify(res)
