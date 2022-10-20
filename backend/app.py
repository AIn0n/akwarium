from flask import Flask
from os import urandom

app = Flask(__name__)

# rationale for that kind of imports:
# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
import hello


app.config["SECRET_KEY"] = urandom(24)
