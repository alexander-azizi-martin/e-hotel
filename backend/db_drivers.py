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
    def check_account_and_role(self, ssn_sin, password, role):
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

    def get_hotel_chain(self, chain_id):
        self.cursor.execute("SELECT * FROM Hotel_Chain WHERE chain_ID = %s", (chain_id,))
        results = self.cursor.fetchone()
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
        query = self.cursor.execute("SELECT role FROM Employee_Role WHERE employee_SSN_SIN=%s AND employee_ID=%s", (employee_SSN_SIN, employee_ID))
        result = query.fetchall()

        roles = [row[0] for row in result]

        # Move the manager role to the first position in the list, if it exists
        if 'manager' in roles:
            roles.remove('manager')
            roles.insert(0, 'manager')

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

    def insert_customer(self, customer_SSN_SIN, password, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date):
        try:
            # Check if the customer already exists in the Customer table or an employee exists with the same SSN_SIN
            existing_customer = self.get_customer(customer_SSN_SIN)
            existing_employee = self.get_employee(customer_SSN_SIN)

            if existing_customer or existing_employee:
                print("Error: Customer or employee with the same SSN/SIN already exists.")

            else:
                # Insert a new customer
                self.cursor.execute("INSERT INTO Customer (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date))
                # Insert a new user
                hashed_password = generate_password_hash(password)
                self.cursor.execute("INSERT INTO Users (user_SSN_SIN, password, role) VALUES (%s, %s, %s)", (customer_SSN_SIN, hashed_password, 'customer'))
                self.commit()

        except Exception as e:
            print("Error inserting customer:", e)

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
                hashed_password = generate_password_hash(password)
                self.cursor.execute("INSERT INTO Users (user_SSN_SIN, password, role) VALUES (%s, %s, %s)", (employee_SSN_SIN, hashed_password, 'employee'))
                self.commit()

        except Exception as e:
            print("Error inserting employee:", e)

    def insert_employee_role(self, employee_SSN_SIN, employee_ID, hotel_ID, role):
        try:
            # Check if the Employee_Role entry already exists with the same role
            existing_employee_role = self.get_employee_role_by_role(employee_SSN_SIN, employee_ID, role)

            if existing_employee_role:
                print("Error: Employee already has this role.")
            else:
                # Insert a new employee role
                self.cursor.execute("INSERT INTO Employee_Role (employee_SSN_SIN, employee_ID, hotel_ID, role) VALUES (%s, %s, %s, %s)",
                                    (employee_SSN_SIN, employee_ID, hotel_ID, role))
                self.commit()

        except Exception as e:
            print("Error inserting employee role:", e)


if __name__ == "__main__":
  db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
  all_hotels = db.get_all_hotels()
  print(all_hotels)
  hotel = db.get_hotel(1021)
  print(hotel)