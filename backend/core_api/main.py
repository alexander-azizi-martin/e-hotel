from flask import Flask, request, jsonify, current_app
from flask_restx import Api, Resource, fields
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os
import json
from flask_cors import CORS
from auth import auth_namespace
from hotel import hotel_namespace
from hotel_chain import hotel_chain_namespace
from room import room_namespace
from booking import booking_namespace
import click

def create_app(config): 
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    JWTManager(app)
    api = Api(app, doc="/docs")
    api.add_namespace(hotel_namespace)
    api.add_namespace(hotel_chain_namespace)
    api.add_namespace(room_namespace)
    api.add_namespace(booking_namespace)
    #api.add_namespace(rental_namespace)
    api.add_namespace(auth_namespace)
    return app