from flask import request
from flask import current_app
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

rental_namespace = Namespace("rental", description="All routes under this namespace concern rental operations.")

rental_model = rental_namespace.model('Rental', {
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

conv_booking_to_rental_model = rental_namespace.conv_booking_to_rental_model('ConvertToRental', {
    'total_paid': fields.Integer(required=True, description='Total amount paid for the rental'),
    'discount': fields.Integer(required=True, description='Discount applied to the rental'),
    'additional_charges': fields.Integer(required=True, description='Additional charges for the rental'),
})

@rental_namespace.route("/rental")
class Rental(Resource):
    @rental_namespace.doc(responses={201: "Created", 400: "Invalid input", 401: "Unauthorized"})
    @rental_namespace.expect(rental_model)
    @jwt_required()
    def post(self):
        token_data = get_jwt()
        if token_data["role"] != "employee":
            return {"message": "Unauthorized!"}, 401

        employee_SSN_SIN = get_jwt_identity()
        data = request.json
        try:
            current_app.db.insert_rental(
                data["base_price"],
                data["date_paid"],
                data["total_paid"],
                data["discount"],
                data["additional_charges"],
                data["check_in_date"],
                data["check_out_date"],
                data["customer_SSN_SIN"],
                data["room_number"],
                data["hotel_ID"],
                data["employee_ID"],
                employee_SSN_SIN
            )
        except Exception as e:
            return {"message": str(e)}, 400

        return {"message": "Rental added successfully."}, 201


@rental_namespace.route("/rentals/<int:customer_SSN_SIN>")
class RentalsByCustomer(Resource):
    @rental_namespace.doc(responses={200: "Success", 401: "Unauthorized", 500: "Internal Server Error"})
    @jwt_required()
    def get(self, customer_SSN_SIN=None):
        token_data = get_jwt()
        role = token_data["role"]
        user_SSN_SIN = get_jwt_identity()

        if role == "customer" and customer_SSN_SIN != user_SSN_SIN:
            return {"message": "Unauthorized!"}, 401

        try:
            if role == "employee" and customer_SSN_SIN is None:
                rentals = current_app.db.get_all_rentals()
            else:
                rentals = current_app.db.get_rentals_by_customer(customer_SSN_SIN)

            parsed_rentals = [
                {
                    "rental_ID": rental[0],
                    "base_price": rental[1],
                    "date_paid": rental[2],
                    "total_paid": rental[3],
                    "discount": rental[4],
                    "additional_charges": rental[5],
                    "check_in_date": rental[6],
                    "check_out_date": rental[7],
                    "customer_SSN_SIN": rental[8],
                    "booking_ID": rental[9],
                    "room_number": rental[10],
                    "hotel_ID": rental[11],
                    "employee_ID": rental[12],
                    "employee_SSN_SIN": rental[13]
                }
                for rental in rentals
            ]

            return parsed_rentals, 200
        except Exception as e:
            return {"message": f"Error getting rentals: {str(e)}"}, 500


@rental_namespace.route("/rental/convert/<int:booking_id>")
class ConvertBookingToRental(Resource):
    @rental_namespace.doc(responses={201: "Created", 400: "Invalid input", 401: "Unauthorized"})
    @jwt_required()
    def post(self, booking_id):
        token_data = get_jwt()
        if token_data["role"] != "employee":
            return {"message": "Unauthorized!"}, 401

        data = request.json
        try:
            current_app.db.convert_booking_to_rental(
                booking_id,
                data.get("total_paid", None),
                data.get("discount", None),
                data.get("additional_charges", None)
            )
        except Exception as e:
            return {"message": str(e)}, 400

        return {"message": "Booking converted to rental successfully."}, 201

