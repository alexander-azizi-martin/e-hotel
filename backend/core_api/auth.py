from flask_restx import Resource, Namespace, fields
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

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

customer_login_model = auth_namespace.model(
    "Login", {"username": fields.String(), "password": fields.String()}
)

@auth_namespace.route("/register")
class Register(Resource):
    @auth_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @auth_namespace.expect(customer_model)
    def post(self):
        """
        Register a new user.
        """
        data = request.json
        username = data.get("username")
        password = data.get("password")
        
        # Validate input
        if not username or not password:
            return {"message": "Username and password are required."}, 400
        
        # Hash password
        hashed_password = generate_password_hash(password, method="sha256")
        
        # Save user to database
        # ...
        
        return {"message": "User registered successfully."}, 200
