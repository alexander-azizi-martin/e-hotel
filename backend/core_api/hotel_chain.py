from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.db_drivers import Database

hotel_chain_namespace = Namespace("hotel_chain", description="All routes under this namespace concern hotel chain operations.")

hotel_chain_model = hotel_chain_namespace.model('HotelChain', {
    'chain_ID': fields.Integer(required=True, description='Hotel chain ID'),
    'name': fields.String(required=True, description='Hotel chain name'),
    'number_of_hotels': fields.Integer(required=True, description='Number of hotels in the chain')
})

@hotel_chain_namespace.route("/hotel_chain")
class HotelChain(Resource):
    @hotel_chain_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @hotel_chain_namespace.expect(hotel_chain_model)
    @jwt_required()
    def post(self):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Save hotel chain to database
        # ...

        return {"message": "Hotel chain added successfully."}, 200

    @hotel_chain_namespace.doc(responses={200: "Success", 400: "Invalid input", 500: "Internal Server Error"})
    @hotel_chain_namespace.expect(hotel_chain_model)
    @jwt_required()
    def put(self):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Update hotel chain in the database
        # ...

        return {"message": "Hotel chain updated successfully."}, 200

@hotel_chain_namespace.route("/hotel_chain/<int:chain_ID>")
class HotelChainByID(Resource):
    @hotel_chain_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def delete(self, chain_ID):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        # Delete hotel chain from the database
        # ...

        return {"message": "Hotel chain deleted successfully."}, 200

