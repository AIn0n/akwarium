from app import app, species_db, users_db
from flask import request

# login part
logged_users = set()

@app.route("/add-species", methods=["POST"])
def add_species():
    # Necessary forms
    name = request.form["name"]
    water_requirements = request.form["water_requirements"]
    required_size:float = request.form["required_size"]

    # Species object creation and insertion
    obj = {
        "name": name,
        "water_requirements": water_requirements,
        "required_size": required_size,
        "list_of_natural_aggressors": []
    }
    species_db.insert_one(obj)

    return "Success", 200

### DOESN'T SEEM TO WORK PROPERLY
@app.route("/add-species-aggressor", methods=["POST"])
def add_species_aggressor():
    # Necessary forms
    subject_name = request.form["subject_name"]
    aggressor_name = request.form["aggressor_name"]

    # Query validation
    species_names = get_species_names()
    if(species_names.count(subject_name) != 1):
        return "Invalid aggression subject name", 419
    if(species_names.count(aggressor_name) != 1):
        return "Invalid aggressor name", 419

    # Aggressor insertion
    users_db.find_one_and_update({
            "name": subject_name
        }, {
            "$push": {"list_of_natural_aggressors": aggressor_name}
        }
    )

    return "Success", 200


@app.route("/species-names", methods=["GET"])
def get_species_names():
    return [x['name'] for x in species_db.find({})]


@app.route("/species-aggressors", methods=["GET"])
def get_species_aggressors():
    name = request.form["name"]
    return species_db.find_one({"name":name})["list_of_natural_aggressors"]


@app.route("/delete-species", methods=["DELETE"])
def delete_species():
    name = request.form["name"]
    species_db.find_one_and_delete({"name": name})
    return "Success", 200