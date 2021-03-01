from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'D:/Documents/INFO3180/info3180-lab4/uploads'
from app import views
