from flask import Flask
import json  # rationale: for reading config.json file
import pymongo  # rationale:

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)
mongo_client = pymongo.MongoClient(app.config["MONGO_API"])
users_db = mongo_client["database"]["users"]

# rationale for that kind of imports:
# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
import log_in as log_in
import aquarium as aquarium