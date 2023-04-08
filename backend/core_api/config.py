import os
from decouple import config
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

class ProdConfig(Config):
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DEBUG = os.getenv('DEBUG')
    SWAGGER_UI_REQUEST_HEADERS = {'Content-Type': 'application/json'}