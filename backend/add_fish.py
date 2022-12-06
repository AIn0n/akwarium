from app import app, users_db, species_db
from flask import make_response, request, redirect, url_for, abort
from bson.objectid import ObjectId
import flask_login as fl

# login part
logged_users = set()


@fl.login_required
@app.route("/add-fish", methods=["POST"])
def add_fish():
    id = fl.current_user.id

    name = request.form["name"]
    species = request.form["species"]
    birth_date = request.form["birth_date"]

    aquarium_name = request.form["aquarium_name"]

    species_names = [x["name"] for x in species_db.find({})]
    if species_names.count(species) != 1:
        return "Invalid species name", 419

    # todo: Replace species string with a species object
    obj = {
        "name": name,
        "species": species,
        "birth_date": birth_date,
        "status": "OK"
    }

    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))},
        {"$push": {"aquarium.$[a].fish": obj}},
        array_filters=[{"a.name": aquarium_name}],
    )

    return "Success", 200
