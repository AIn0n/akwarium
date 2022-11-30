from app import app, fish_db, users_db
from flask import make_response, request, redirect, url_for, abort
from bson.objectid import ObjectId
import flask_login as fl

# login part
logged_users = set()


@app.route("/add-fish", methods=["POST"])
def add_fish():
    id = fl.current_user.id

    name = request.form["name"]
    species = request.form["species"]
    birth_date = request.form["birth_date"]

    aquarium_name = request.form["aquarium_name"]

    obj = {
        "name": name,
        "species": species,
        "birth_date": birth_date,
        "status": "OK",
    }

    users_db.find_one_and_update
    (
        {"_id": ObjectId(str(id)), "aquarium.name": aquarium_name},
        {"$push": {"aquarium.$.fish": obj}},
    )

    print(obj)

    print(
        users_db.find_one(
            {"_id": ObjectId(str(id)), "aquarium.name": aquarium_name}
        )
    )

    return "Success", 200


# @app.route("/fish", methods=["GET"])
# def fish():
#     id = fl.current_user.id
#     aquarium_name = request.form["aquarium_name"]

#     x =  users_db.find_one
#     (
#         {
#             "_id": ObjectId(str(id)),
#             "aquarium.name": aquarium_name
#         }
#     )
#     return x
