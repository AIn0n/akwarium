from app import app, users_db, species_db
from flask import request
from bson.objectid import ObjectId
import flask_login as fl
import log as log
import datetime


def find_fish(name, aquarium):
    for fish in aquarium["fish"]:
        if fish["name"] == name:
            return fish
    return


def find_aquarium(name, user):
    for aquarium in user["aquarium"]:
        if aquarium["name"] == name:
            return aquarium
    return


@fl.login_required
@app.route("/add-fish", methods=["POST"])
def add_fish():
    id = fl.current_user.id
    name = request.form["name"]
    species = request.form["species"]
    week_age = int(request.form["week_age"])
    aquarium_name = request.form["aquarium_name"]

    # Species name validation
    species_names = [x["name"] for x in species_db.find({})]
    if species not in species_names:
        return "Invalid species name", 419

    this_user = users_db.find_one({"_id": ObjectId(str(id))})

    # Aquarium name validation
    this_aquarium = find_aquarium(aquarium_name, this_user)
    if not this_aquarium:
        return "Invalid aquarium name", 420

    # Fish name validation
    if find_fish(name, this_aquarium):
        return "A fish with this name already exists", 421

    # Issue handling
    issues = []
    for fish in this_aquarium["fish"]:
        if (
            fish["species"]
            in species_db.find_one({"name": species})["incompatibilities"]
        ):
            new_issue_this = {
                "type": "INCOMPATIBLE_SPECIES",
                "problem_subject": fish["name"],
                "message": "Incompatible species with " + fish["name"],
            }
            new_issue_opposite = {
                "type": "INCOMPATIBLE_SPECIES",
                "problem_subject": name,
                "message": "Incompatible species with " + name,
            }
            issues.append(new_issue_this)

            users_db.update_one(
                {"_id": ObjectId(str(id))},
                {
                    "$push": {
                        "aquarium.$[a].fish.$[b].issues": new_issue_opposite
                    }
                },
                array_filters=[
                    {"a.name": aquarium_name},
                    {"b.name": fish["name"]},
                ],
            )

    now = datetime.datetime.now()
    try:
        birth_date = now - datetime.timedelta(weeks=week_age)
    except TypeError:
        return "Invalid fish age data type", 422

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
    log.water_update(id, aquarium_name)

    return "Success", 200


@fl.login_required
@app.route("/delete-fish", methods=["DELETE"])
def delete_fish():
    try:
        id = fl.current_user.id
    except AttributeError:
        return "Attribute error. User probably not logged in.", 424

    name = request.form["name"]
    aquarium_name = request.form["aquarium_name"]

    this_user = users_db.find_one({"_id": ObjectId(str(id))})

    # Aquarium name validation
    this_aquarium = find_aquarium(aquarium_name, this_user)
    if not this_aquarium:
        return "Invalid aquarium name", 420

    # Fish name validation
    if not find_fish(name, this_aquarium):
        return "No such fish exists", 423

    # Issue handling
    for fish in this_aquarium["fish"]:
        for issue in fish["issues"]:
            if (
                issue["type"] == "INCOMPATIBLE_SPECIES"
                and issue["problem_subject"] == name
            ):
                users_db.update_one(
                    {"_id": ObjectId(str(id))},
                    {
                        "$pull": {
                            "aquarium.$[a].fish.$[b].issues": {
                                "problem_subject": name,
                                "type": "INCOMPATIBLE_SPECIES",
                            }
                        }
                    },
                    array_filters=[
                        {"a.name": aquarium_name},
                        {"b.name": fish["name"]},
                    ],
                )

    users_db.update_one(
        {"_id": ObjectId(str(id))},
        {"$pull": {"aquarium.$[a].fish": {"name": name}}},
        array_filters=[{"a.name": aquarium_name}],
    )
    log.water_update(id, aquarium_name)
    return "Success", 200
