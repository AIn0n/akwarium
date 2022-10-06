from app import app
from flask import make_response, request

i = 0


@app.route("/hello", methods=["GET"])
def hello():
    global i
    name = request.form["name"]
    i += 1
    return make_response({"hello": name, "counter": i}, 200)
