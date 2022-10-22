from flask import Flask
import json # rationale: for reading config.json file

app = Flask(__name__)

app.config.from_file("config.json", load=json.load)

# rationale for that kind of imports:
# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
import log_in as log_in



