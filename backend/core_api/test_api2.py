import unittest
from flask import current_app
from flask_testing import TestCase
from main import create_app
from db.db_drivers import Database
from config import TestConfig
from flask_jwt_extended import decode_token, get_jwt
import json

app_instance = None

class TestAvailableRooms(TestCase):

    def create_app(self):
        global app_instance

        if app_instance is None:
            app_instance = create_app(TestConfig)

        return app_instance

    def test_get_available_rooms(self):
        # Test data
        start_date = "2023-04-03"
        end_date = "2023-04-25"

        # Make a request to the /room/available-rooms endpoint
        response = self.client.get(f"/room/available-rooms?start_date={start_date}&end_date={end_date}")

        # Check if the response is successful
        self.assertEqual(response.status_code, 200, f"Failed to get available rooms: {response.data}")

        # Check if the response contains the expected data
        expected_data = [
            {"country": "USA", "state_province": "NY", "city": "New York", "available_rooms": 1},
            {"country": "USA", "state_province": "CA", "city": "San Francisco", "available_rooms": 2},
        ]
        self.assertEqual(response.json, expected_data, "Response data does not match expected data")

if __name__ == "__main__":
    unittest.main()
