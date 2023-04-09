from sqlalchemy.sql.expression import text
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import psycopg2
import datetime
import random
import traceback
import bcrypt
import hashlib

load_dotenv()
# SETUP
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
TEST_DB_NAME = os.getenv('TEST_DB_NAME')

# We need an object oriented way to connect to and communicate with the database.
class Database(object): 
    # Constructor to make a connection to the database and return an object to execute queries with.
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host, port = port)
        self.cursor = self.connection.cursor()
        self.connection_details = f"dbname={dbname} user={user} password={password} host={host} port={port}"

    # Methods to close connection and commit changes to the database.
    def close(self):
      self.connection.close()

    def commit(self):
      self.connection.commit()
    
    def clear_table(self, table_name):
        try:
            # Clear the table
            self.cursor.execute(f"DELETE FROM {table_name}")
            self.commit()
            print(f"{table_name} table cleared.")

        except Exception as e:
            print(f"Error clearing {table_name} table:", e)
            self.connection.rollback()

    ### Action methods on the database.
    # Method checks whether a user exists and returns their role if they exist.
    def check_account_and_role(self, ssn_sin, password, role):
        print(password)
        self.cursor.execute("SELECT * FROM Users WHERE user_SSN_SIN=%s", (ssn_sin,))
        result = self.cursor.fetchone()

        if not result:
            return ["Invalid SSN/SIN"]
        hashed_pass = result[1]

        if check_password_hash(hashed_pass, password):
            user_type = result[2]
            if user_type == role:
                if user_type == "customer":
                    self.cursor.execute("SELECT * FROM Customer WHERE customer_SSN_SIN=%s", (ssn_sin,))
                elif user_type == "employee":
                    self.cursor.execute("SELECT * FROM Employee WHERE employee_SSN_SIN=%s", (ssn_sin,))
                
                user_info = self.cursor.fetchone()
                return ["Found User", user_type, user_info]
            else:
                return ["Invalid Role"]
        else:
            return ["Invalid Password"]

    def get_all_hotels(self):
        self.cursor.execute("SELECT * FROM Hotel")
        results = self.cursor.fetchall()
        return results

    def get_hotel(self, id):
        self.cursor.execute("SELECT * FROM Hotel WHERE hotel_ID = %s", (id,))
        results = self.cursor.fetchone()
        return results

    def get_all_hotel_chains(self):
        self.cursor.execute("SELECT * FROM Hotel_Chain")
        results = self.cursor.fetchall()
        return results

    def get_hotel_chain(self, chain_id=None, name=None):
        if chain_id is not None and name is not None:
            self.cursor.execute("""
                SELECT * FROM Hotel_Chain 
                WHERE chain_ID = %s OR name = %s
            """, (chain_id, name))
        elif chain_id is not None:
            self.cursor.execute("SELECT * FROM Hotel_Chain WHERE chain_ID = %s", (chain_id,))
        elif name is not None:
            self.cursor.execute("SELECT * FROM Hotel_Chain WHERE name = %s", (name,))
        else:
            raise ValueError("Either chain_id or name must be provided.")

        results = self.cursor.fetchall()
        return results

    def get_employees_by_hotel_id(self, hotel_id):
        self.cursor.execute("SELECT * FROM Employee WHERE hotel_ID = %s", (hotel_id,))
        results = self.cursor.fetchall()
        return results

    def get_all_employees(self): 
      self.cursor.execute("SELECT * FROM Employee")
      results = self.cursor.fetchall()
      return results

    def get_employee(self, employee_ssn_sin, employee_id=None):
        if employee_id is None:
            self.cursor.execute("SELECT * FROM Employee WHERE employee_SSN_SIN = %s", (employee_ssn_sin,))
        else:
            self.cursor.execute("SELECT * FROM Employee WHERE employee_SSN_SIN = %s AND employee_ID = %s", (employee_ssn_sin, employee_id))
        results = self.cursor.fetchone()
        return results

    def get_employee_roles(self, employee_SSN_SIN, employee_ID):
        self.cursor.execute("SELECT role FROM Employee_Role WHERE Employee_Role.employee_SSN_SIN=%s AND Employee_Role.employee_ID=%s", (employee_SSN_SIN, employee_ID))
        result = self.cursor.fetchall()

        roles = [row[0].lower().strip() for row in result]

        return roles

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
        results = self.cursor.fetchone()
        return results

    def get_all_amenities(self):
        self.cursor.execute("SELECT * FROM Amenity")
        results = self.cursor.fetchall()
        return results

    def get_customer(self, customer_ssn_sin):
        self.cursor.execute("SELECT * FROM Customer WHERE customer_SSN_SIN = %s", (customer_ssn_sin,))
        results = self.cursor.fetchall()
        return results
    
    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM Customer")
        results = self.cursor.fetchall()
        return results

    def get_all_bookings(self):
        self.cursor.execute("SELECT * FROM Booking")
        results = self.cursor.fetchall()
        return results

    def get_booking(self, booking_id):
        self.cursor.execute("SELECT * FROM Booking WHERE booking_ID = %s", (booking_id,))
        results = self.cursor.fetchone()
        return results

    def get_all_rentals(self):
        self.cursor.execute("SELECT * FROM Rental")
        results = self.cursor.fetchall()
        return results

    def get_rental(self, rental_id):
        self.cursor.execute("SELECT * FROM Rental WHERE rental_ID = %s", (rental_id,))
        results = self.cursor.fetchall()
        return results


    ### INSERTION & UPDATION FUNCTIONS
    def insert_hotel(self, hotel_id, chain_id=None, number_of_rooms=None, address_street_name=None, address_street_number=None, 
                    address_city=None, address_province_state=None, address_country=None, contact_email=None, star_rating=None):
        try:
            # Check if the hotel already exists
            existing_hotel = self.get_hotel(hotel_id)
            if existing_hotel:
                # Update the hotel information if it exists
                update_query = "UPDATE Hotel SET "
                update_values = []

                # Create a dictionary with column names and parameter values
                columns_and_values = {
                    "chain_ID": chain_id,
                    "number_of_rooms": number_of_rooms,
                    "address_street_name": address_street_name,
                    "address_street_number": address_street_number,
                    "address_city": address_city,
                    "address_province_state": address_province_state,
                    "address_country": address_country,
                    "contact_email": contact_email,
                    "star_rating": star_rating
                }

                # Iterate through the dictionary and build the query
                for column, value in columns_and_values.items():
                    if value is not None:
                        update_query += f"{column} = %s, "
                        update_values.append(value)

                # Remove the trailing comma and space
                update_query = update_query.rstrip(', ')
                update_query += " WHERE hotel_ID = %s"
                update_values.append(hotel_id)

                self.cursor.execute(update_query, tuple(update_values))
            else:
                # Insert a new hotel if it doesn't exist
                self.cursor.execute("""
                    INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, 
                                      address_city, address_province_state, address_country, contact_email, star_rating) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (hotel_id, chain_id, number_of_rooms, address_street_name, address_street_number, 
                          address_city, address_province_state, address_country, contact_email, star_rating))
            self.commit()
        except Exception as e:
            print("Error inserting or updating hotel:", e)
            self.connection.rollback()


    def insert_hotel_chain(self, chain_id, name=None, number_of_hotels=None):
        try:
            # Check if the hotel chain already exists
            existing_hotel_chain = self.get_hotel_chain(chain_id)
            if existing_hotel_chain:
                # Update the hotel chain information if it exists
                update_query = "UPDATE Hotel_Chain SET "
                update_values = []

                # Create a dictionary with column names and parameter values
                columns_and_values = {
                    "name": name,
                    "number_of_hotels": number_of_hotels
                }

                # Iterate through the dictionary and build the query
                for column, value in columns_and_values.items():
                    if value is not None:
                        update_query += f"{column} = %s, "
                        update_values.append(value)

                # Remove the trailing comma and space
                update_query = update_query.rstrip(', ')
                update_query += " WHERE chain_ID = %s"
                update_values.append(chain_id)

                self.cursor.execute(update_query, tuple(update_values))
            else:
                # Insert a new hotel chain if it doesn't exist
                self.cursor.execute("INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (%s, %s, %s)",
                                    (chain_id, name, number_of_hotels))
            self.commit()
        except Exception as e:
            print("Error inserting or updating hotel chain:", e)
            self.connection.rollback()


    def insert_customer(self, customer_SSN_SIN, password, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date):
        try:
            # Check if the customer already exists in the Customer table or an employee exists with the same SSN_SIN
            existing_customer = self.get_customer(customer_SSN_SIN)
            existing_employee = self.get_employee(customer_SSN_SIN)

            if existing_customer or existing_employee:
                return (False, "Error: Customer or Employee with the same SSN/SIN already exists.")

            else:
                # Insert a new customer
                self.cursor.execute("INSERT INTO Customer (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date))
                # Insert a new user
                self.cursor.execute("INSERT INTO Users (user_SSN_SIN, password, role) VALUES (%s, %s, %s)", (customer_SSN_SIN, password, 'customer'))
                self.commit()

        except Exception as e:
            self.connection.rollback()
            return (False, f"Error inserting customer: {e}")

        return (True, "Customer successfully registered")


    def insert_employee(self, employee_SSN_SIN, employee_ID, password, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager):
        try:
            # Check if the employee already exists in the Employee table or an customer exists with the same SSN_SIN
            existing_customer = self.get_customer(employee_SSN_SIN)
            existing_employee = self.get_employee(employee_SSN_SIN, employee_ID)

            if existing_employee or existing_customer:
                print("Error: Employee already exists.")

            else:
                # Insert a new employee
                self.cursor.execute("INSERT INTO Employee (employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager))
                # Insert a new user
                self.cursor.execute("INSERT INTO Users (user_SSN_SIN, password, role) VALUES (%s, %s, %s)", (employee_SSN_SIN, password, 'employee'))
                self.commit()

        except Exception as e:
            print("Error inserting employee:", e)
            self.connection.rollback()


    def insert_employee_role(self, employee_SSN_SIN, employee_ID, role):
        try:
            # Check if the Employee_Role entry already exists with the same employee and role
            self.cursor.execute(
                "SELECT COUNT(*) FROM Employee_Role WHERE employee_SSN_SIN = %s AND employee_ID = %s AND role = %s",
                (employee_SSN_SIN, employee_ID, role)
            )
            count = self.cursor.fetchone()[0]

            if count > 0:
                print("Error: Employee already has this role.")
            else:
                # Insert a new employee role
                self.cursor.execute(
                    "INSERT INTO Employee_Role (employee_SSN_SIN, employee_ID, role) VALUES (%s, %s, %s)",
                    (employee_SSN_SIN, employee_ID, role)
                )
                self.connection.commit()
                print("Employee role inserted successfully.")
        except Exception as e:
            print("Error inserting employee role:", e)
            self.connection.rollback()
    

    def insert_room(self, room_number, hotel_id, room_capacity, view_type, price_per_night, is_extendable, room_problems=None):
        try:
            # Check if the room already exists
            existing_room = self.get_room(room_number, hotel_id)
            if existing_room:
                # Update the room information if it exists
                update_query = "UPDATE Room SET "
                update_values = []

                # Create a dictionary with column names and parameter values
                columns_and_values = {
                    "room_capacity": room_capacity,
                    "view_type": view_type,
                    "price_per_night": price_per_night,
                    "is_extendable": is_extendable,
                    "room_problems": room_problems
                }

                # Iterate through the dictionary and build the query
                for column, value in columns_and_values.items():
                    if value is not None:
                        update_query += f"{column} = %s, "
                        update_values.append(value)

                # Remove the trailing comma and space
                update_query = update_query.rstrip(', ')
                update_query += " WHERE room_number = %s AND hotel_ID = %s"
                update_values.append(room_number)
                update_values.append(hotel_id)

                self.cursor.execute(update_query, tuple(update_values))
            else:
                # Insert a new room if it doesn't exist
                self.cursor.execute("""
                    INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (room_number, hotel_id, room_capacity, view_type, price_per_night, is_extendable, room_problems))
            self.commit()
        except Exception as e:
            print("Error inserting or updating room:", e)
            self.connection.rollback()


    def insert_booking(self, booking_id, customer_SSN_SIN, room_number, hotel_id, check_in_date, check_out_date):
        if check_in_date >= check_out_date:
            print("Error: Check-in date must be earlier than check-out date.")
            return

        if check_in_date + datetime.timedelta(days=1) == check_out_date:
            print("Error: Check-in date and check-out date cannot be the same day.")
            return

        try:
            # Check if the customer exists
            existing_customer = self.get_customer(customer_SSN_SIN)
            if not existing_customer:
                print("Error: Customer does not exist.")
                return

            # Check if the room exists
            existing_room = self.get_room(room_number, hotel_id)
            if not existing_room:
                print("Error: Room does not exist.")
                return

            # Check for duplicate bookings
            self.cursor.execute("""
                SELECT * FROM Booking 
                WHERE room_number = %s
                AND hotel_ID = %s
                AND (
                    (scheduled_check_in_date <= %s AND scheduled_check_out_date >= %s) 
                    OR (scheduled_check_out_date >= %s AND scheduled_check_out_date <= %s) 
                    OR (scheduled_check_in_date >= %s AND scheduled_check_in_date <= %s)
                )
                AND canceled = False
            """, (room_number, hotel_id, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date))

            existing_booking = self.cursor.fetchone()
            if existing_booking:
                print("Error: Duplicate booking found.")
                return

            # Insert the booking
            self.cursor.execute("""
                INSERT INTO Booking (booking_ID, booking_date, scheduled_check_in_date, scheduled_check_out_date, canceled, customer_SSN_SIN, room_number, hotel_ID) 
                VALUES (%s, %s, %s, %s, false, %s, %s, %s)
            """, (booking_id, datetime.date.today(), check_in_date, check_out_date, customer_SSN_SIN, room_number, hotel_id))
            self.commit()
            print("Booking created successfully.")
        except Exception as e:
            print("Error inserting booking:", e)
            self.connection.rollback()
    

    def convert_booking_to_rental(self, booking_id, total_paid=None, discount=None, additional_charges=None):
        try:
            # Check if the booking exists and is not canceled
            existing_booking = self.get_booking(booking_id)
            if not existing_booking or existing_booking[4]:
                print("Error: Booking does not exist or has been canceled.")
                return

            # Choose a random employee to assign to the rental
            employees = self.get_employees_by_hotel_id(existing_booking[7])
            if not employees:
                print("Error: No employees found for this hotel.")
                return
            employee = random.choice(employees)

            # Create the rental
            rental_data = {
                'base_price': self.get_room(existing_booking[6], existing_booking[7])[4],
                'date_paid': datetime.date.today(),
                'total_paid': 0 if total_paid is None else total_paid,
                'discount': 0 if discount is None else discount,
                'additional_charges': 0 if additional_charges is None else additional_charges,
                'check_in_date': existing_booking[2],
                'check_out_date': existing_booking[3],
                'customer_SSN_SIN': existing_booking[5],
                'booking_ID': existing_booking[0],
                'room_number': existing_booking[6],
                'hotel_ID': existing_booking[7],
                'employee_ID': employee[1],
                'employee_SSN_SIN': employee[0]
            }
            self.cursor.execute("""
                INSERT INTO Rental (base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN)
                VALUES (%(base_price)s, %(date_paid)s, %(total_paid)s, %(discount)s, %(additional_charges)s, %(check_in_date)s, %(check_out_date)s, %(customer_SSN_SIN)s, %(booking_ID)s, %(room_number)s, %(hotel_ID)s, %(employee_ID)s, %(employee_SSN_SIN)s)
            """, rental_data)
            self.commit()

            print(f"Booking converted to rental successfully. Assigned to employee {employee[1]}.")

        except Exception as e:
            print("Error converting booking to rental:", e)
            traceback.print_exc()
            self.connection.rollback()


    def create_rental(self, room_number, hotel_id, customer_SSN_SIN, check_in_date, check_out_date, total_paid=None, discount=None, additional_charges=None):
        if check_in_date >= check_out_date:
            print("Error: Check-in date must be earlier than check-out date.")
            return

        if check_in_date + datetime.timedelta(days=1) == check_out_date:
            print("Error: Check-in date and check-out date cannot be the same day.")
            return
        
        try:
            # Check if the customer exists
            existing_customer = self.get_customer(customer_SSN_SIN)
            if not existing_customer:
                print("Error: Customer does not exist.")
                return

            # Check if the room exists
            existing_room = self.get_room(room_number, hotel_id)
            if not existing_room:
                print("Error: Room does not exist.")
                return

            # Check for duplicate rentals
            self.cursor.execute("""
                SELECT * FROM Rental 
                WHERE room_number = %s
                AND hotel_ID = %s
                AND (
                    (check_in_date <= %s AND check_out_date >= %s) 
                    OR (check_out_date >= %s AND check_out_date <= %s) 
                    OR (check_in_date >= %s AND check_in_date <= %s)
                )
            """, (room_number, hotel_id, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date))
            
            existing_rental = self.cursor.fetchone()
            if existing_rental:
                print("Error: Duplicate booking found.")
                return

            # Choose a random employee to assign to the rental
            employees = self.get_employees_by_hotel_id(hotel_id)
            if not employees:
                print("Error: No employees found for this hotel.")
                return
            employee = random.choice(employees)

            # Create the rental
            rental_data = {
                'base_price': existing_room[4],
                'date_paid': datetime.date.today(),
                'total_paid': 0 if total_paid is None else total_paid,
                'discount': 0 if discount is None else discount,
                'additional_charges': 0 if additional_charges is None else additional_charges,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'customer_SSN_SIN': customer_SSN_SIN,
                'booking_ID': None,
                'room_number': room_number,
                'hotel_ID': hotel_id,
                'employee_ID': employee[1],
                'employee_SSN_SIN': employee[0]
            }
            self.cursor.execute("""
                INSERT INTO Rental (base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN)
                VALUES (%(base_price)s, %(date_paid)s, %(total_paid)s, %(discount)s, %(additional_charges)s, %(check_in_date)s, %(check_out_date)s, %(customer_SSN_SIN)s, %(booking_ID)s, %(room_number)s, %(hotel_ID)s, %(employee_ID)s, %(employee_SSN_SIN)s)
            """, rental_data)
            self.commit()

            print(f"Rental created successfully. Assigned to employee {employee[1]}.")

        except Exception as e:
            print("Error creating rental:", e)
            traceback.print_exc()
            self.connection.rollback()

    # ONLY RETURNS HOTELS THAT HAVE ROOMS
    def search_hotels_and_rooms(self, city=None, star_rating=None, view_type=None, room_capacity=None, is_extendable=None, price_per_night=None):
        query = """
            SELECT h.hotel_ID, h.chain_ID, h.number_of_rooms, h.address_street_name, h.address_street_number, 
                  h.address_city, h.address_province_state, h.address_country, h.contact_email, h.star_rating, 
                  r.room_number, r.room_capacity, r.view_type, r.price_per_night, r.is_extendable, r.room_problems
            FROM Hotel h
            JOIN Room r ON h.hotel_ID = r.hotel_ID
            WHERE 1 = 1
        """

        params = {}

        if city is not None:
            query += " AND h.address_city = %(city)s"
            params['city'] = city

        if star_rating is not None:
            query += " AND h.star_rating = %(star_rating)s"
            params['star_rating'] = star_rating

        if view_type is not None:
            query += " AND r.view_type = %(view_type)s"
            params['view_type'] = view_type

        if room_capacity is not None:
            query += " AND r.room_capacity = %(room_capacity)s"
            params['room_capacity'] = room_capacity

        if is_extendable is not None:
            query += " AND r.is_extendable = %(is_extendable)s"
            params['is_extendable'] = is_extendable

        if price_per_night is not None:
            query += " AND r.price_per_night = %(price_per_night)s"
            params['price_per_night'] = price_per_night

        query += " ORDER BY h.hotel_ID, r.room_number"

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        hotels = []
        current_hotel = None

        for row in rows:
            if current_hotel is None or row[0] != current_hotel['hotel_ID']:
                current_hotel = {
                    'hotel_ID': row[0],
                    'chain_ID': row[1],
                    'number_of_rooms': row[2],
                    'address_street_name': row[3],
                    'address_street_number': row[4],
                    'address_city': row[5],
                    'address_province_state': row[6],
                    'address_country': row[7],
                    'contact_email': row[8],
                    'star_rating': row[9],
                    'rooms': []
                }

                hotels.append(current_hotel)

            current_hotel['rooms'].append({
                'room_number': row[10],
                'room_capacity': row[11],
                'view_type': row[12],
                'price_per_night': row[13],
                'is_extendable': row[14],
                'room_problems': row[15]
            })

        return hotels

    def delete_customer(self, ssn_sin): 
        print("running")
        self.cursor.execute("DELETE FROM Customer WHERE customer_SSN_SIN = %s", (ssn_sin,))
        self.cursor.execute("DELETE FROM Users WHERE user_SSN_SIN = %s", (ssn_sin,))
        self.commit()

    def delete_employee(self, ssn_sin): 
        print("running")
        self.cursor.execute("DELETE FROM Employee WHERE employee_SSN_SIN = %s", (ssn_sin,))
        self.cursor.execute("DELETE FROM Users WHERE user_SSN_SIN = %s", (ssn_sin,))
        self.commit()
    
    def delete_hotel_chain(self, chain_id):
        try:
            self.cursor.execute("DELETE FROM Hotel_Chain WHERE chain_ID = %s", (chain_id,))
            self.commit()
        except Exception as e:
            print("Error deleting hotel chain:", e)
            self.connection.rollback()
    
    def delete_hotel(self, hotel_id):
        try:
            self.cursor.execute("DELETE FROM Hotel WHERE hotel_ID = %s", (hotel_id,))
            self.commit()
        except Exception as e:
            print("Error deleting hotel chain:", e)
            self.connection.rollback() 


#db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
#test_db = Database(TEST_DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
