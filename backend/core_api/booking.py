from flask import Flask, request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from db.db_drivers import Database

booking_namespace = Namespace("booking", description="All routes under this namespace concern booking operations.")

booking_model = booking_namespace.model('Booking', {
    'booking_ID': fields.Integer(required=True, description='Booking ID'),
    'booking_date': fields.Date(required=True, description='Date of booking'),
    'scheduled_check_in_date': fields.Date(required=True, description='Scheduled check-in date'),
    'scheduled_check_out_date': fields.Date(required=True, description='Scheduled check-out date'),
    'canceled': fields.Boolean(required=True, description='Indicates if the booking is canceled'),
    'customer_SSN_SIN': fields.Integer(required=True, description='Customer SSN/SIN'),
    'room_number': fields.Integer(required=True, description='Room number'),
    'hotel_ID': fields.Integer(required=True, description='Hotel ID')
})

@booking_namespace.route("/booking")
class Booking(Resource):
    @booking_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @booking_namespace.expect(booking_model)
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        current_user = Database.get_user_by_id(user_id)

        if not current_user or current_user["role"] != "customer":
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Save booking to database
        # ...

        return {"message": "Booking added successfully."}, 200

    @booking_namespace.doc(responses={200: "Success", 400: "Invalid input", 500: "Internal Server Error"})
    @booking_namespace.expect(booking_model)
    @jwt_required()
    def put(self):
        user_id = get_jwt_identity()
        current_user = Database.get_user_by_id(user_id)

        if not current_user or current_user["role"] != "customer":
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Check if the booking belongs to the current user
        # ...

        # Update booking in the database
        # ...

        return {"message": "Booking updated successfully."}, 200

@booking_namespace.route("/booking/<int:booking_ID>")
class BookingByID(Resource):
    @booking_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def delete(self, booking_ID):
        user_id = get_jwt_identity()
        current_user = Database.get_user_by_id(user_id)

        if not current_user:
            return {"message": "Unauthorized!"}, 401

        is_manager = False
        if current_user["role"] == "employee":
            current_employee = Database.get_employee_by_id(user_id)
            is_manager = current_employee["is_manager"]

        # Check if the current user is a manager and the booking is for their hotel
        # ...

        # Check if the booking belongs to the current user
        # ...

        # Delete booking from the database
        # ...

        return {"message": "Booking deleted successfully."}, 200
