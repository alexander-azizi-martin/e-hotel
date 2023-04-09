from flask import Flask, request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from db.db_drivers import Database

hotel_namespace = Namespace("hotel", description="All routes under this namespace concern hotel operations.")

hotel_model = hotel_namespace.model('Hotel', {
    'hotel_ID': fields.Integer(required=True, description='Hotel ID'),
    'chain_ID': fields.Integer(required=True, description='Hotel chain ID'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms in the hotel'),
    'address_street_name': fields.String(required=True, description='Street name of the hotel address'),
    'address_street_number': fields.Integer(required=True, description='Street number of the hotel address'),
    'address_city': fields.String(required=True, description='City of the hotel address'),
    'address_province_state': fields.String(required=True, description='Province or state of the hotel address'),
    'address_country': fields.String(required=True, description='Country of the hotel address'),
    'contact_email': fields.String(required=True, description='Contact email of the hotel'),
    'star_rating': fields.Integer(required=True, description='Star rating of the hotel')
})

@hotel_namespace.route("/hotel")
class Hotel(Resource):
    @hotel_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @hotel_namespace.expect(hotel_model)
    @jwt_required()
    def post(self):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Save hotel to database
        # ...

        return {"message": "Hotel added successfully."}, 200

    @hotel_namespace.doc(responses={200: "Success", 400: "Invalid input", 500: "Internal Server Error"})
    @hotel_namespace.expect(hotel_model)
    @jwt_required()
    def put(self):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Update hotel in the database
        # ...

        return {"message": "Hotel updated successfully."}, 200

@hotel_namespace.route("/hotel/<int:hotel_ID>")
class HotelByID(Resource):
    @hotel_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def delete(self, hotel_ID):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        # Delete hotel from the database
        # ...

        return {"message": "Hotel deleted successfully."}, 200
