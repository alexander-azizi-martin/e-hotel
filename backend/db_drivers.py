from sqlalchemy.sql.expression import text
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import psycopg2
import datetime

load_dotenv()

# SETUP
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# We need an object oriented way to connect to and communicate with the database.
class Database(object): 
    # Constructor to make a connection to the database and return an object to execute queries with.
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host, port = port)
        self.cursor = self.connection.cursor()

    # Methods to close connection and commit changes to the database.
    def close(self):
      self.connection.close()

    def commit(self):
      self.connection.commit()
    
    ### Action methods on the database.
    # Method checks whether a user exists and returns their role if they exist.
    def check_account_and_role(self, username, password): 
        query = self.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = query.fetchall()
        print(result)
        if not result: 
          return ["Invalid Username"]
        hashed_pass = result[2]
        if check_password_hash(password, hashed_pass):
          user_type = result[3]
          return ["Found User", user_type]
    
    # Add methods here as we use them.
    def search(**kwargs): 
        pass

    def get_all_hotels(self):
        self.cursor.execute("SELECT * FROM Hotel")
        results = self.cursor.fetchall()
        return results

    def get_hotel(self, id):
        self.cursor.execute("SELECT * FROM Hotel WHERE hotel_ID = %s", (id,))
        results = self.cursor.fetchall()
        return results

    def get_all_hotel_chains(self):
        self.cursor.execute("SELECT * FROM Hotel_Chain")
        results = self.cursor.fetchall()
        return results

    def get_hotel_chain(self, chain_id):
        self.cursor.execute("SELECT * FROM Hotel_Chain WHERE chain_ID = %s", (chain_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_employees(self):
        self.cursor.execute("SELECT * FROM Employee")
        results = self.cursor.fetchall()
        return results

    def get_employee(self, employee_ssn_sin, employee_id):
        self.cursor.execute("SELECT * FROM Employee WHERE employee_SSN_SIN = %s AND employee_ID = %s", (employee_ssn_sin, employee_id))
        results = self.cursor.fetchall()
        return results

    def get_all_hotel_phone_numbers(self):
        self.cursor.execute("SELECT * FROM Hotel_Phone_Number")
        results = self.cursor.fetchall()
        return results

    def get_hotel_phone_number(self, hotel_id):
        self.cursor.execute("SELECT * FROM Hotel_Phone_Number WHERE hotel_ID = %s", (hotel_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_hotel_chain_central_office_addresses(self):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Central_Office_Address")
        results = self.cursor.fetchall()
        return results

    def get_hotel_chain_central_office_address(self, chain_id):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Central_Office_Address WHERE chain_ID = %s", (chain_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_hotel_chain_contact_emails(self):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Contact_Email")
        results = self.cursor.fetchall()
        return results

    def get_hotel_chain_contact_email(self, chain_id):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Contact_Email WHERE chain_ID = %s", (chain_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_hotel_chain_phone_numbers(self):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Phone_Number")
        results = self.cursor.fetchall()
        return results

    def get_hotel_chain_phone_number(self, chain_id):
        self.cursor.execute("SELECT * FROM Hotel_Chain_Phone_Number WHERE chain_ID = %s", (chain_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_rooms(self):
        self.cursor.execute("SELECT * FROM Room")
        results = self.cursor.fetchall()
        return results

    def get_room(self, room_number, hotel_id):
        self.cursor.execute("SELECT * FROM Room WHERE room_number = %s AND hotel_ID = %s", (room_number, hotel_id))
        results = self.cursor.fetchall()
        return results

    def get_all_amenities(self):
        self.cursor.execute("SELECT * FROM Amenity")
        results = self.cursor.fetchall()
        return results

    def get_customer(self, customer_ssn_sin):
        self.cursor.execute("SELECT * FROM Customer WHERE customer_SSN_SIN = %s", (customer_ssn_sin,))
        results = self.cursor.fetchall()
        return results

    def get_all_bookings(self):
        self.cursor.execute("SELECT * FROM Booking")
        results = self.cursor.fetchall()
        return results

    def get_booking(self, booking_id):
        self.cursor.execute("SELECT * FROM Booking WHERE booking_ID = %s", (booking_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_rentals(self):
        self.cursor.execute("SELECT * FROM Rental")
        results = self.cursor.fetchall()
        return results

    def get_rental(self, rental_id):
        self.cursor.execute("SELECT * FROM Rental WHERE rental_ID = %s", (rental_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM Users")
        results = self.cursor.fetchall()
        return results

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        results = self.cursor.fetchall()
        return results
    
    def insert_hotel_chain(self, chain_ID, name, number_of_hotels):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (%s, %s, %s);",
                                    (chain_ID, name, number_of_hotels))
                return "Successfully inserted into Hotel_Chain"
        except Exception as e:
            return str(e)

    def insert_hotel(self, hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating):
      try:
          with self.connection:
              self.cursor.execute("INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                                  (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating))
              return "Successfully inserted into Hotel"
      except Exception as e:
          return str(e)

    def insert_employee(self, employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Employee (employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                                    (employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager))
                return "Successfully inserted into Employee"
        except Exception as e:
            return str(e)

    def insert_employee_role(self, employee_SSN_SIN, employee_ID, hotel_ID, role):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Employee_Role (employee_SSN_SIN, employee_ID, hotel_ID, role) VALUES (%s, %s, %s, %s);",
                                    (employee_SSN_SIN, employee_ID, hotel_ID, role))
                return "Successfully inserted into Employee_Role"
        except Exception as e:
            return str(e)

    def insert_hotel_phone_number(self, hotel_ID, phone_number):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (%s, %s);",
                                    (hotel_ID, phone_number))
                return "Successfully inserted into Hotel_Phone_Number"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_central_office_address(self, chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country) VALUES (%s, %s, %s, %s, %s, %s);",
                                    (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country))
                return "Successfully inserted into Hotel_Chain_Central_Office_Address"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_contact_email(self, chain_ID, contact_email):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (%s, %s);",
                                    (chain_ID, contact_email))
                return "Successfully inserted into Hotel_Chain_Contact_Email"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_phone_number(self, chain_ID, phone_number):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (%s, %s);",
                                    (chain_ID, phone_number))
                return "Successfully inserted into Hotel_Chain_Phone_Number"
        except Exception as e:
            return str(e)

    def insert_room(self, room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems):
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                                    (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems))
                return "Successfully inserted into Room"
        except Exception as e:
            return str(e)
    
    def insert_customer(self, customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date):
        try:
            self.cursor.execute("INSERT INTO Customer (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                                (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date))
            self.connection.commit()
            return "Successfully inserted into Customer"
        except Exception as e:
            return str(e)

    def insert_booking(self, booking_date, scheduled_check_in_date, scheduled_check_out_date, customer_SSN_SIN, room_number, hotel_ID):
        try:
            self.cursor.execute("INSERT INTO Booking (booking_date, scheduled_check_in_date, scheduled_check_out_date, customer_SSN_SIN, room_number, hotel_ID) VALUES (%s, %s, %s, %s, %s, %s);",
                                (booking_date, scheduled_check_in_date, scheduled_check_out_date, customer_SSN_SIN, room_number, hotel_ID))
            self.connection.commit()
            return "Successfully inserted into Booking"
        except Exception as e:
            return str(e)

    def insert_rental(self, base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN):
        try:
            self.cursor.execute("INSERT INTO Rental (base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                                (base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN))
            self.connection.commit()
            return "Successfully inserted into Rental"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_central_office_address(self, chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country):
        try:
            self.cursor.execute("INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country) VALUES (%s, %s, %s, %s, %s, %s);",
                                (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country))
            self.connection.commit()
            return "Successfully inserted into Hotel_Chain_Central_Office_Address"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_contact_email(self, chain_ID, contact_email):
        try:
            self.cursor.execute("INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (%s, %s);",
                                (chain_ID, contact_email))
            self.connection.commit()
            return "Successfully inserted into Hotel_Chain_Contact_Email"
        except Exception as e:
            return str(e)

    def insert_hotel_chain_phone_number(self, chain_ID, phone_number):
        try:
            self.cursor.execute("INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (%s, %s);",
                                (chain_ID, phone_number))
            self.connection.commit()
            return "Successfully inserted into Hotel_Chain_Phone_Number"
        except Exception as e:
            return str(e)
    
    def insert_user(self, username, password, role):
        try:
            hashed_password = generate_password_hash(password)
            self.cursor.execute("INSERT INTO Users (username, password, role) VALUES (%s, %s, %s);",
                                (username, hashed_password, role))
            self.connection.commit()
            return "Successfully inserted into Users"
        except Exception as e:
            return str(e)

db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
all_hotels = db.get_all_hotels()
print(all_hotels)
hotel = db.get_hotel(1021)
print(hotel)