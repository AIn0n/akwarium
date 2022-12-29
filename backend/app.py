from flask import Flask
from flask_cors import CORS
import json  # rationale: for reading config.json file
import pymongo  # rationale:

app = Flask(__name__)
CORS(app, supports_credentials=True)
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (("http://localhost:5173", "http://localhost:5000"),)
app.config.from_file("config.json", load=json.load)
mongo_client = pymongo.MongoClient(app.config["MONGO_API"])
logs_db = mongo_client["database"]["logs"]
users_db = mongo_client["database"]["users"]
device_db = mongo_client["database"]["device"]
species_db = mongo_client["database"]["species"]

# rationale for that kind of imports:
# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
import log_in as log_in
import account as account
import aquarium as aquarium
import add_fish as add_fish
import species as species
import log as log
