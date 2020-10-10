from flask import Flask
import logging
app = Flask(__name__)
logger = logging.Logger(__name__)
from app.routes import *
