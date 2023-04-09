from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.db_drivers import Database

room_namespace = Namespace("rooms", description="All routes under this namespace concern room operations.")

room_model = room_namespace.model('Room', {
    'room_number': fields.Integer(required=True, description='Room number'),
    'hotel_ID': fields.Integer(required=True, description='Hotel ID'),
    'room_capacity': fields.Integer(required=True, description='Capacity of the room'),
    'view_type': fields.String(required=True, description='View type of the room'),
    'price_per_night': fields.Integer(required=True, description='Price per night for the room'),
    'is_extendable': fields.Boolean(required=True, description='Indicates if the room is extendable'),
    'room_problems': fields.String(required=False, description='Problems associated with the room')
})

@room_namespace.route("/<int:hotel_ID>/rooms")
class RoomList(Resource):
    @room_namespace.doc(responses={200: "Success", 400: "Invalid input", 409: "Conflict", 500: "Internal Server Error"})
    @room_namespace.expect(room_model)
    @jwt_required()
    def post(self, hotel_ID):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Save room to database
        # ...

        return {"message": "Room added successfully."}, 200

    @room_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def get(self, hotel_ID):
        # Retrieve list of rooms for the given hotel_ID from the database
        # ...

        return {"message": "List of rooms retrieved successfully.", "data": room_data}, 200

@room_namespace.route("/<int:hotel_ID>/rooms/<int:room_number>")
class Room(Resource):
    @room_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def get(self, hotel_ID, room_number):
        # Retrieve room information for the given room_number and hotel_ID from the database
        # ...

        return {"message": "Room information retrieved successfully.", "data": room_data}, 200

    @room_namespace.doc(responses={200: "Success", 400: "Invalid input", 500: "Internal Server Error"})
    @room_namespace.expect(room_model)
    @jwt_required()
    def put(self, hotel_ID, room_number):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        data = request.json
        # Update room in the database
        # ...

        return {"message": "Room updated successfully."}, 200

    @room_namespace.doc(responses={200: "Success", 404: "Not found", 500: "Internal Server Error"})
    @jwt_required()
    def delete(self, hotel_ID, room_number):
        employee_id = get_jwt_identity()
        current_employee = Database.get_employee_by_id(employee_id)

        if not current_employee or not current_employee["is_manager"]:
            return {"message": "Unauthorized!"}, 401

        # Delete room from the database
        # ...

        return {"message": "Room deleted successfully."}, 200