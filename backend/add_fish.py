from app import app, users_db, species_db
from flask import request
from bson.objectid import ObjectId
import flask_login as fl


@fl.login_required
@app.route("/add-fish", methods=["POST"])
def add_fish():
    id = fl.current_user.id

    # Necessary forms
    name = request.form["name"]
    species = request.form["species"]
    birth_date = request.form["birth_date"]
    aquarium_name = request.form["aquarium_name"]

    # Species name validation
    species_names = [x["name"] for x in species_db.find({})]
    if species_names.count(species) != 1:
        return "Invalid species name", 419

    this_user = users_db.find_one({"_id": ObjectId(str(id))})

    # Aquarium name validation
    this_aquarium = None
    for aquarium in this_user["aquarium"]:
        if aquarium["name"] == aquarium_name:
            this_aquarium = aquarium
    if this_aquarium == None:
        return "Invalid aquarium name", 420

    # Fish name validation
    for fish in this_aquarium["fish"]:
        if fish["name"] == name:
            return "A fish with this name already exists", 421

    # Issue handling
    issues = []
    for fish in this_aquarium["fish"]:
        if (
            fish["species"]
            in species_db.find_one({"name": species})["incompatibilities"]
        ):
            issues.append("Incompatible species with " + fish["name"])
            users_db.update_one(
                {"_id": ObjectId(str(id))},
                {
                    "$push": {
                        "aquarium.$[a].fish.$[b].issues": "Incompatible species with "
                        + name
                    }
                },
                array_filters=[
                    {"a.name": aquarium_name},
                    {"b.name": fish["name"]},
                ],
            )

    # todo: Replace species string with a species object
    obj = {
        "name": name,
        "species": species,
        "birth_date": birth_date,
        "status": "OK",
        "issues": issues,
    }

    users_db.find_one_and_update(
        {"_id": ObjectId(str(id))},
        {"$push": {"aquarium.$[a].fish": obj}},
        array_filters=[{"a.name": aquarium_name}],
    )

    return "Success", 200


@fl.login_required
@app.route("/delete-fish", methods=["DELETE"])
def delete_fish():
    id = fl.current_user.id
    name = request.form["name"]
    aquarium_name = request.form["aquarium_name"]

    # Doesn't seem to delete for some reason
    result = users_db.find_one_and_update(
        {"_id": ObjectId(str(id))},
        {"$pull": {"aquarium.$[a].fish": {"name": name}}},
        array_filters=[{"a.name": aquarium_name}],
    )

    print(f"The collections are ")
    users_db.list_indexes()

    # print(f"The result is {result}")

    return "Success", 200
