from flask import Flask, request, jsonify
from flask import current_app
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_jwt

rental_namespace = Namespace("rental", description="All routes under this namespace concern rental operations.")

rental_model = rental_namespace.model('Rental', {
    'rental_ID': fields.Integer(required=True, description='Rental ID'),
    'base_price': fields.Integer(required=True, description='Base price of the rental'),
    'date_paid': fields.Date(required=True, description='Date the rental was paid'),
    'total_paid': fields.Integer(required=True, description='Total amount paid for the rental'),
    'discount': fields.Integer(required=True, description='Discount applied to the rental'),
    'additional_charges': fields.Integer(required=True, description='Additional charges for the rental'),
    'check_in_date': fields.Date(required=True, description='Check-in date'),
    'check_out_date': fields.Date(required=True, description='Check-out date'),
    'customer_SSN_SIN': fields.Integer(required=True, description='Customer SSN/SIN'),
    'booking_ID': fields.Integer(required=True, description='Booking ID'),
    'room_number': fields.Integer(required=True, description='Room number'),
    'hotel_ID': fields.Integer(required=True, description='Hotel ID'),
    'employee_ID': fields.Integer(required=True, description='Employee ID'),
    'employee_SSN_SIN': fields.Integer(required=True, description='Employee SSN/SIN')
})

@rental_namespace.route("/rental")
class Rental(Resource):
    pass

@rental_namespace.route("/rental/<int:rental_ID>")
class RentalByID(Resource):
    pass
