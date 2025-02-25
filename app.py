from flask import Flask, request
from dotenv import load_dotenv

from auth import validate_credentials

load_dotenv()

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
  username = request.form["username"]
  password = request.form["password"]
  return str(validate_credentials(username, password))
