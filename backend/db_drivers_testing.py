import os
import datetime
from dotenv import load_dotenv
from db_drivers import Database
load_dotenv()

### TESTING THE DB DRIVERS ###  
def test_insert_hotel_chain(db):
    print("Inserting new hotel chain...")
    db.insert_hotel_chain(1, "Luxury Hotels", 10)
    print("Inserted hotel chain with chain_ID 1.")

    print("Updating hotel chain...")
    db.insert_hotel_chain(1, "Luxury Hotels International", 11)
    print("Updated hotel chain with chain_ID 1.")

    print("Printing all hotel chains...")
    hotel_chains = db.get_all_hotel_chains()
    assert len(hotel_chains) == 1
    assert hotel_chains[0][0] == 1
    assert hotel_chains[0][1] == "Luxury Hotels International"
    assert hotel_chains[0][2] == 11
    print("test 1 passed")

def test_insert_hotel(db):
    print("Inserting new hotel...")
    db.insert_hotel(1, 1, 100, "Sunset Boulevard", 123, "Los Angeles", "California", "USA", "contact@luxuryhotels.com", 5)
    print("Inserted hotel with hotel_ID 1.")

    print("Updating hotel...")
    db.insert_hotel(1, 1, 110, "Sunset Boulevard", 123, "Los Angeles", "California", "USA", "contact@luxuryhotels.com", 5)
    print("Updated hotel with hotel_ID 1.")

    print("Printing all hotels...")
    hotels = db.get_all_hotels()
    assert len(hotels) == 1
    assert hotels[0][0] == 1
    assert hotels[0][1] == 1
    assert hotels[0][2] == 110
    assert hotels[0][3] == "Sunset Boulevard"
    assert hotels[0][4] == 123
    assert hotels[0][5] == "Los Angeles"
    assert hotels[0][6] == "California"
    assert hotels[0][7] == "USA"
    assert hotels[0][8] == "contact@luxuryhotels.com"
    assert hotels[0][9] == 5
    print("test 2 passed")

def test_insert_customer(db):
    print("Inserting new customer...")
    db.insert_customer(123456789, "password", "John", "Doe", "123 Main St", 1, "Anytown", "ON", "Canada", "2022-01-01")
    print("Inserted customer with SSN/SIN 123456789.")

    print("Attempting to insert duplicate customer...")
    db.insert_customer(123456789, "new_password", "Jane", "Doe", "456 Main St", 2, "Othertown", "ON", "Canada", "2022-02-01")

    print("Printing all customers...")
    customers = db.get_all_customers()
    print(customers)
    assert len(customers) == 1
    assert customers[0][0] == 123456789
    assert customers[0][1] == "John"
    assert customers[0][2] == "Doe"
    assert customers[0][3] == "123 Main St"
    assert customers[0][4] == 1
    assert customers[0][5] == "Anytown"
    assert customers[0][6] == "ON"
    assert customers[0][7] == "Canada"
    assert customers[0][8] == datetime.date(2022, 1, 1)
    print("test_insert_customer passed")

def test_insert_employee(db):
    print("Inserting new employee...")
    db.insert_employee(987654321, 1, "password", "John", "Smith", "123 Main St", 1, "Anytown", "ON", "Canada", 1, True)
    print("Inserted employee with SSN/SIN 987654321 and employee ID 1.")

    print("Attempting to insert duplicate employee...")
    db.insert_employee(987654321, 1, "new_password", "Jane", "Smith", "456 Main St", 2, "Othertown", "ON", "Canada", 2, False)

    print("Printing all employees...")
    employees = db.get_all_employees()
    print(employees)
    assert len(employees) == 1
    assert employees[0][0] == 987654321
    assert employees[0][1] == 1
    assert employees[0][2] == "John"
    assert employees[0][3] == "Smith"
    assert employees[0][4] == "123 Main St"
    assert employees[0][5] == 1
    assert employees[0][6] == "Anytown"
    assert employees[0][7] == "ON"
    assert employees[0][8] == "Canada"
    assert employees[0][9] == 1
    assert employees[0][10] == True
    print("test_insert_employee passed")

def test_check_account_and_role(db):
    print("Testing check_account_and_role...")

    # Test case 1: Valid customer credentials
    result = db.check_account_and_role(123456789, "password", "customer")
    assert result[0] == "Found User"
    assert result[1] == "customer"
    print("Test case 1 passed")

    # Test case 2: Invalid customer password
    assert db.check_account_and_role(123456789, "wrong_password", "customer") == ["Invalid Password"]
    print("Test case 2 passed")

    # Test case 3: Valid employee credentials
    result = db.check_account_and_role(987654321, "password", "employee")
    assert result[0] == "Found User"
    assert result[1] == "employee"
    print("Test case 3 passed")

    # Test case 4: Invalid employee password
    assert db.check_account_and_role(987654321, "wrong_password", "employee") == ["Invalid Password"]
    print("Test case 4 passed")

    # Test case 5: Non-existent user SSN/SIN
    assert db.check_account_and_role(111111111, "password", "customer") == ["Invalid SSN/SIN"]
    print("Test case 5 passed")

    # Test case 6: Incorrect role for user
    assert db.check_account_and_role(123456789, "password", "employee") == ["Invalid Role"]
    print("Test case 6 passed")

    print("All test cases for check_account_and_role passed")

def test_insert_employee_role(db):
    print("Inserting new employee role...")
    db.insert_employee_role(987654321, 1, "Receptionist")
    print("Inserted employee role Receptionist for employee ID 1.")

    print("Inserting new employee role...")
    db.insert_employee_role(987654321, 1, "Manager")
    print("Inserted employee role Manager for employee ID 1.")

    print("Inserting new employee role...")
    db.insert_employee_role(987654321, 1, "Housekeeping")
    print("Inserted employee role Housekeeping for employee ID 1.")

    print("Inserting duplicate employee role...")
    db.insert_employee_role(987654321, 1, "Receptionist")
    print("Attempting to insert duplicate employee role Receptionist for employee ID 1.")

    print("Printing all employee roles...")
    employee_roles = db.get_employee_roles(987654321, 1)
    print(employee_roles)
    assert len(employee_roles) == 3
    assert "receptionist" in employee_roles
    assert "housekeeping" in employee_roles
    assert employee_roles.count("receptionist") == 1
    assert 'manager' == employee_roles[0]
    print("test_insert_employee_role passed")

def test_insert_room(db):
    print("Inserting new room...")
    db.insert_room(101, 1, 2, "Ocean", 250, True, "None")
    print("Inserted room with room_number 101.")

    print("Updating room...")
    db.insert_room(101, 1, 3, "Ocean", 300, True, "None")
    print("Updated room with room_number 101.")

    print("Printing all rooms...")
    rooms = db.get_all_rooms()
    assert len(rooms) == 1
    assert rooms[0][0] == 101
    assert rooms[0][1] == 1
    assert rooms[0][2] == 3
    assert rooms[0][3] == "Ocean"
    assert rooms[0][4] == 300
    assert rooms[0][5] == True
    assert rooms[0][6] == "None"
    print("test_insert_room passed")

def test_insert_booking(db):
    print("Inserting new booking...")
    db.insert_booking(123456789, 101, 1, datetime.date(2023, 4, 10), datetime.date(2023, 4, 14))
    print("Inserted booking with customer SSN/SIN 123456789 and room number 101.")

    print("Attempting to insert duplicate booking...")
    db.insert_booking(123456789, 101, 1, datetime.date(2023, 4, 11), datetime.date(2023, 4, 13))

    print("Attempting to insert booking with invalid check-in and check-out dates...")
    db.insert_booking(123456789, 101, 1, datetime.date(2023, 4, 14), datetime.date(2023, 4, 10))

    print("Attempting to insert booking with same check-in and check-out date...")
    db.insert_booking(123456789, 101, 1, datetime.date(2023, 4, 10), datetime.date(2023, 4, 10))

    print("Printing all bookings...")
    bookings = db.get_all_bookings()
    print(bookings)
    assert len(bookings) == 1
    assert bookings[0][0] == 1
    assert bookings[0][1] == datetime.date.today()
    assert bookings[0][2] == datetime.date(2023, 4, 10)
    assert bookings[0][3] == datetime.date(2023, 4, 14)
    assert bookings[0][4] == False
    assert bookings[0][5] == 123456789
    assert bookings[0][6] == 101
    assert bookings[0][7] == 1
    print("test_insert_booking passed")

if __name__ == "__main__":
    # Replace the following with your actual database connection details
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    TEST_DB_NAME = os.getenv('TEST_DB_NAME')

    # Create a Database instance and run the test functions
    test_db = Database(TEST_DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    test_db.cursor.execute("DROP TABLE IF EXISTS Hotel_Chain, Hotel, Employee, Employee_Role, Hotel_Phone_Number, Hotel_Chain_Central_Office_Address, Hotel_Chain_Contact_Email, Hotel_Chain_Phone_Number, Room, Amenity, Has_Amenity, Customer, Booking, Rental, Users CASCADE")
    test_db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Hotel_Chain (
        chain_ID INT,
        name VARCHAR(50) NOT NULL,
        number_of_hotels INT NOT NULL,
        PRIMARY KEY (chain_ID)
        );

        CREATE TABLE IF NOT EXISTS Hotel (
        hotel_ID INT,
        chain_ID INT,
        number_of_rooms INT,
        address_street_name VARCHAR(50) NOT NULL,
        address_street_number INT NOT NULL,
        address_city VARCHAR(50) NOT NULL,
        address_province_state VARCHAR(50) NOT NULL,
        address_country VARCHAR(50) NOT NULL,
        contact_email VARCHAR(50) NOT NULL,
        star_rating INT NOT NULL,
        PRIMARY KEY (hotel_ID),
        FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID) ON DELETE CASCADE,
        CONSTRAINT uc_address UNIQUE (address_street_name, address_street_number, address_city, address_province_state, address_country)
        );

        CREATE TABLE IF NOT EXISTS Employee (
        employee_SSN_SIN INT,
        employee_ID INT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address_street_name VARCHAR(50) NOT NULL,
        address_street_number INT NOT NULL,
        address_city VARCHAR(50) NOT NULL,
        address_province_state VARCHAR(50) NOT NULL,
        address_country VARCHAR(50) NOT NULL,
        hotel_ID INT NOT NULL,
        is_manager BOOLEAN NOT NULL,
        PRIMARY KEY (employee_SSN_SIN, employee_ID),
        FOREIGN KEY (hotel_ID) REFERENCES Hotel(hotel_ID)
        );

        CREATE TABLE Employee_Role (
        employee_SSN_SIN INT,
        employee_ID INT,
        role VARCHAR(50) NOT NULL,
        PRIMARY KEY (employee_SSN_SIN, employee_ID, role),
        FOREIGN KEY (employee_SSN_SIN, employee_ID) REFERENCES Employee(employee_SSN_SIN, employee_ID)
        );

        CREATE TABLE IF NOT EXISTS Hotel_Phone_Number (
        hotel_ID INT,
        phone_number VARCHAR(20),
        PRIMARY KEY (hotel_ID, phone_number),
        FOREIGN KEY (hotel_ID) REFERENCES Hotel(hotel_ID)
        );

        CREATE TABLE IF NOT EXISTS Hotel_Chain_Central_Office_Address (
        chain_ID INT,
        address_street_name VARCHAR(50) NOT NULL,
        address_street_number INT NOT NULL,
        address_city VARCHAR(50) NOT NULL,
        address_province_state VARCHAR(50) NOT NULL,
        address_country VARCHAR(50) NOT NULL,
        PRIMARY KEY (chain_ID),
        FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
        );

        CREATE TABLE IF NOT EXISTS Hotel_Chain_Contact_Email (
        chain_ID INT,
        contact_email VARCHAR(50) NOT NULL,
        PRIMARY KEY (chain_ID),
        FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
        );

        CREATE TABLE IF NOT EXISTS Hotel_Chain_Phone_Number (
        chain_ID INT,
        phone_number VARCHAR(12),
        PRIMARY KEY (chain_ID, phone_number),
        FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
        );

        CREATE TABLE IF NOT EXISTS Room (
        room_number INT,
        hotel_ID INT,
        room_capacity INT NOT NULL,
        view_type VARCHAR(50) NOT NULL,
        price_per_night INT NOT NULL,
        is_extendable BOOLEAN NOT NULL,
        room_problems TEXT,
        PRIMARY KEY (room_number, hotel_ID),
        FOREIGN KEY (hotel_ID) REFERENCES Hotel(hotel_ID) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Amenity (
        amenity_id INT,
        amenity_name VARCHAR(50) NOT NULL,
        PRIMARY KEY (amenity_id)
        );

        CREATE TABLE IF NOT EXISTS Has_Amenity (
        amenity_id INT,
        hotel_id INT,
        room_number INT,
        PRIMARY KEY (amenity_id, hotel_id, room_number),
        FOREIGN KEY (hotel_id, room_number) REFERENCES Room(hotel_ID, room_number)
        );

        CREATE TABLE IF NOT EXISTS Customer (
            customer_SSN_SIN INT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            address_street_name VARCHAR(50) NOT NULL,
            address_street_number INT NOT NULL,
            address_city VARCHAR(50) NOT NULL,
            address_province_state VARCHAR(50) NOT NULL,
            address_country VARCHAR(50) NOT NULL,
            registration_date DATE NOT NULL,
            PRIMARY KEY (customer_SSN_SIN)
        );

        CREATE TABLE IF NOT EXISTS Booking (
            booking_ID SERIAL,
            booking_date DATE NOT NULL,
            scheduled_check_in_date DATE NOT NULL,
            scheduled_check_out_date DATE NOT NULL,
            canceled BOOLEAN NOT NULL DEFAULT false,
            customer_SSN_SIN INT,
            room_number INT,
            hotel_ID INT,
            PRIMARY KEY (booking_ID),
            FOREIGN KEY (customer_SSN_SIN) REFERENCES Customer(customer_SSN_SIN),
            FOREIGN KEY (room_number, hotel_ID) REFERENCES Room(room_number, hotel_ID)
        );

        CREATE TABLE IF NOT EXISTS Rental (
        rental_ID SERIAL,
        base_price INT NOT NULL,
        date_paid DATE NOT NULL,
        total_paid INT NOT NULL,
        discount INT NOT NULL,
        additional_charges INT NOT NULL,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL,
        customer_SSN_SIN INT,
        booking_ID INT,
        room_number INT,
        hotel_ID INT,
        employee_ID INT,
        employee_SSN_SIN INT,
        PRIMARY KEY (rental_ID),
        FOREIGN KEY (customer_SSN_SIN) REFERENCES Customer(customer_SSN_SIN),
        FOREIGN KEY (employee_SSN_SIN, employee_ID) REFERENCES Employee(employee_SSN_SIN, employee_ID),
        FOREIGN KEY (booking_ID) REFERENCES Booking(booking_ID),
        FOREIGN KEY (room_number, hotel_ID) REFERENCES Room(room_number, hotel_ID)
        );

        CREATE TABLE IF NOT EXISTS Users (
            user_SSN_SIN INT PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(10) NOT NULL,
            CHECK (role = 'customer' OR role = 'employee')
        );
        """)
    test_db.commit()

    test_insert_hotel_chain(test_db)
    test_insert_hotel(test_db)
    test_insert_customer(test_db)
    test_insert_employee(test_db)
    test_check_account_and_role(test_db)
    test_insert_employee_role(test_db)
    test_insert_room(test_db)
    test_insert_booking(test_db)
    print("--------------------------------")
    print("ALL TESTS PASSED")

    # Close the database connection
    test_db.close()

