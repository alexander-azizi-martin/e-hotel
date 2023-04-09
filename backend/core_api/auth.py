from flask_restx import Resource, Namespace, fields
from flask import current_app
from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import hashlib

auth_namespace = Namespace("auth", description="All routes under this namespace concern authentication of customers and employees.")

customer_model = auth_namespace.model('Customer', {
    'customer_SSN_SIN': fields.Integer(required=True, description='Customer SSN/SIN'),
    'first_name': fields.String(required=True, description='First name of the customer'),
    'last_name': fields.String(required=True, description='Last name of the customer'),
    'password': fields.String(required=True, description='Password of the customer'), 
    'address_street_name': fields.String(required=True, description='Street name of the customer address'),
    'address_street_number': fields.Integer(required=True, description='Street number of the customer address'),
    'address_city': fields.String(required=True, description='City of the customer address'),
    'address_province_state': fields.String(required=True, description='Province or state of the customer address'),
    'address_country': fields.String(required=True, description='Country of the customer address')
})

employee_model = auth_namespace.model('Employee', {
    'employee_SSN_SIN': fields.Integer(required=True, description='Employee SSN/SIN'),
    'employee_ID': fields.Integer(required=True, description='Employee ID'),
    'first_name': fields.String(required=True, description='First name of the employee'),
    'last_name': fields.String(required=True, description='Last name of the employee'),
    'password': fields.String(required=True, description='Password of the employee'),
    'address_street_name': fields.String(required=True, description='Street name of the employee address'),
    'address_street_number': fields.Integer(required=True, description='Street number of the employee address'),
    'address_city': fields.String(required=True, description='City of the employee address'),
    'address_province_state': fields.String(required=True, description='Province or state of the employee address'),
    'address_country': fields.String(required=True, description='Country of the employee address'),
    'hotel_ID': fields.Integer(required=True, description='Hotel ID where the employee works'),
    'is_manager': fields.Boolean(required=True, description='Indicates if the employee is a manager'),
    'role': fields.String(required=True, description='Role of the employee at the hotel')
})

login_model = auth_namespace.model("Login", {
    "user_SSN_SIN": fields.String(),
    "password": fields.String(),
    "role": fields.String()
})

@auth_namespace.route("/customers")
class CustomerRegistration(Resource):
    @auth_namespace.expect(customer_model)
    def post(self):

        data = request.json

        required_fields = [
            'customer_SSN_SIN', 'first_name', 'last_name', 'password', 'address_street_name',
            'address_street_number', 'address_city', 'address_province_state', 'address_country'
        ]

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return {"message": f"Missing required fields: {', '.join(missing_fields)}"}, 400

        ssn_sin = data["customer_SSN_SIN"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]
        address_street_name = data["address_street_name"]
        address_street_number = data["address_street_number"]
        address_city = data["address_city"]
        address_province_state = data["address_province_state"]
        address_country = data["address_country"]
        registration_date = datetime.today()

        hashed_password = generate_password_hash(password)

        success, message = current_app.db.insert_customer(
            ssn_sin, hashed_password, first_name,
            last_name, address_street_name,
            address_street_number, address_city,
            address_province_state, address_country,
            registration_date
        )

        if success:
            return {"message": message}, 200
        else:
            return {"message": message}, 500


@auth_namespace.route("/employees")
class EmployeeRegistration(Resource):
    @auth_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @auth_namespace.expect(employee_model)
    def post(self):
        """
        Register a new employee.
        """
        data = request.json

        required_fields = [
            'employee_SSN_SIN', 'employee_ID', 'first_name', 'last_name', 'password', 'address_street_name',
            'address_street_number', 'address_city', 'address_province_state', 'address_country',
            'hotel_ID', 'is_manager', 'role'
        ]

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return {"message": f"Missing required fields: {', '.join(missing_fields)}"}, 400

        ssn_sin = data["employee_SSN_SIN"]
        employee_id = data["employee_ID"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]
        address_street_name = data["address_street_name"]
        address_street_number = data["address_street_number"]
        address_city = data["address_city"]
        address_province_state = data["address_province_state"]
        address_country = data["address_country"]
        hotel_id = data["hotel_ID"]
        is_manager = data["is_manager"]
        role = data["role"]

        try:
            hashed_password = generate_password_hash(password)
            current_app.db.insert_employee(
                ssn_sin, employee_id, hashed_password, first_name,
                last_name, address_street_name,
                address_street_number, address_city,
                address_province_state, address_country,
                hotel_id, is_manager
            )

            current_app.db.insert_employee_role(
                employee_SSN_SIN=ssn_sin, employee_ID=employee_id, role=role
            )

            return {"message": "Employee registered successfully."}, 200

        except Exception as e:
            return {"message": f"Error: {str(e)}"}, 500

@auth_namespace.route("/login")
class Login(Resource):
    @auth_namespace.doc(responses={200: "Success", 400: "Invalid input", 401: "Unauthorized", 500: "Internal Server Error"})
    @auth_namespace.expect(login_model)
    def post(self):
        data = request.json
        user_ssn_sin = data.get("user_SSN_SIN")
        password = data.get("password")
        role = data.get("role")

        # Validate input
        if not user_ssn_sin or not password or not role:
            return {"message": "User SSN/SIN, password, and role are required."}, 400

        # Check if the user exists in the database and verify the role
        result = current_app.db.check_account_and_role(user_ssn_sin, password, role)
        if result[0] == "Invalid SSN/SIN" or result[0] == "Invalid Password" or result[0] == "Invalid Role":
            return {"message": result[0]}, 401

        # Create the JWT token
        token_data = {
            "user_ssn_sin": user_ssn_sin,
            "role": role
        }
        access_token = create_access_token(identity=token_data)

        # Return the access token
        return {"access_token": access_token}, 200