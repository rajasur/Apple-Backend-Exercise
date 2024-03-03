from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize cache dictionary
app.config['CACHE'] = {}

from app import routes