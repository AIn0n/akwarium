from app import app, users_db, device_db
from flask import request, jsonify
import flask_login as fl
from bson.objectid import ObjectId

@app.route("/add_aquarium", methods=["POST"])
@fl.login_required
def add_aquarium():
    id = fl.current_user.id
    name = request.form["name"]
    height = request.form["height"]
    width = request.form["width"]
    length = request.form["length"]
    heater_power = request.form["heater_power"]
    luminocity = request.form["luminocity"]
    pump_power = request.form["pump_power"]
    filter = request.form["filter"]
    obj = {
        "name":name,
        "height": height,
        "width": width,
        "length": length,
        "image":"https://alerybka.pl/wp-content/uploads/2021/09/dojrzale-akwarium.jpeg",
        "heater_power": heater_power,
        "luminocity": luminocity,
        "pump_power": pump_power,
        "filter": filter,
        "fish":[]
    }
    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))}, {"$push": {"aquarium": obj}}
    )
    return "Success", 200

@app.route("/aquarium", methods=["GET"])
@fl.login_required
def aquarium():
    id = fl.current_user.id
    x = users_db.find_one({"_id": ObjectId(str(id))})
    return x["aquarium"]

@app.route("/aquarium_simple", methods=["POST"])
def aquarium_simple():
    x = users_db.find_one({"nick": "john_doe"})
    return x["aquarium"]

@app.route("/devices", methods = ['GET'])
@fl.login_required
def device():
    types = ['filter', 'light', 'pump', 'heater']
    res = {}
    for type in types:
        res[type]=[]
        x = device_db.find({'type':type})
        for el in x:
            el['_id'] = str(el['_id'])
            res[type].append(el)
    return jsonify(res)