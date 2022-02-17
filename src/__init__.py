from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

app = Flask(__name__)

from src.main.routes import main
app.register_blueprint(main)