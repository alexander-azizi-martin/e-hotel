from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os
import json
from flask_cors import CORS
from auth import auth_namespace

def create_app(config): 
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    api = Api(app, doc="/docs")
    #api.add_namespace(hotel_namespace)
    #api.add_namespace(hotel_chain_namespace)
    #api.add_namespace(room_namespace)
    #api.add_namespace(booking_namespace)
    #api.add_namespace(rental_namespace)
    api.add_namespace(auth_namespace)
    return app