from app import app, species_db
from flask import request, jsonify
import flask_login as fl


@fl.login_required
@app.route("/add-species", methods=["POST"])
def add_species():
    # Necessary forms
    name = request.form["name"]

    min_KH: float = request.form["min_KH"]
    min_GH: float = request.form["min_GH"]
    min_NO3: float = request.form["min_NO3"]
    min_NO2: float = request.form["min_NO2"]
    min_pH: float = request.form["min_pH"]

    max_KH: float = request.form["max_KH"]
    max_GH: float = request.form["max_GH"]
    max_NO3: float = request.form["max_NO3"]
    max_NO2: float = request.form["max_NO2"]
    max_pH: float = request.form["max_pH"]

    required_size: float = request.form["required_size"]
    image_URL = request.form["image_URL"]

    # Species insertion

    species_db.insert_one(
        {
            "name": name,
            "water_requirements": {
                "min": {
                    "KH": min_KH,
                    "GH": min_GH,
                    "NO3": min_NO3,
                    "NO2": min_NO2,
                    "pH": min_pH,
                },
                "max": {
                    "KH": max_KH,
                    "GH": max_GH,
                    "NO3": max_NO3,
                    "NO2": max_NO2,
                    "pH": max_pH,
                },
            },
            "required_size": required_size,
            "incompatibilities": [],
            "image_URL": image_URL,
        }
    )
    return "Success", 200


@app.route("/change-species-image", methods=["POST"])
@fl.login_required
def change_species_image():
    # Necessary forms
    name = request.form["name"]
    image_URL = request.form["image_URL"]
    # Database update
    filter = {"name": name}
    update = {"$set": {"image_URL": image_URL}}
    species_db.update_one(filter, update)
    return "Success", 200


@fl.login_required
@app.route("/add-incompatibilities", methods=["POST"])
def add_incompatibilities():
    # Necessary forms
    subject_name = request.form["subject_name"]
    aggressor_name = request.form["aggressor_name"]

    # Query validation
    species_names = get_species_names()
    if subject_name not in species_names != 1:
        return "Invalid aggression subject name", 419
    if aggressor_name not in species_names != 1:
        return "Invalid aggressor name", 419

    # Mutual incompatibility insertion
    species_db.find_one_and_update(
        {"name": subject_name},
        {"$push": {"incompatibilities": aggressor_name}},
    )
    species_db.find_one_and_update(
        {"name": aggressor_name},
        {"$push": {"incompatibilities": subject_name}},
    )

    return "Success", 200


# Returns the names of all existing species
@app.route("/species-names", methods=["GET"])
def get_species_names():
    return [x["name"] for x in species_db.find({})]


# Returns a detailed list of existing species
@app.route("/species", methods=["GET"])
def get_species():
    res = list(species_db.find({}))
    for elem in res:
        elem["_id"] = str(elem["_id"])
    return res


# Returns a single species by name
@app.route("/species/<name>", methods=["GET"])
def get_species_by_name(name=None):
    species = species_db.find_one({"name": name})
    if not species:
        return "No such species"
    # Stringifying the _id to make the object serialisable
    species["_id"] = str(species["_id"])
    return jsonify(species)


@app.route("/incompatibilities/<name>", methods=["GET"])
def get_species_incompatibilities(name=None):
    return (
        species_db.find_one({"name": name})["incompatibilities"]
        or "No such species"
    )


@fl.login_required
@app.route("/delete-species", methods=["DELETE"])
def delete_species():
    name = request.form["name"]
    species_db.find_one_and_delete({"name": name})
    return "Success", 200
