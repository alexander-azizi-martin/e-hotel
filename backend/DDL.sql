CREATE TABLE Hotel_Chain (
  chain_ID INT,
  name VARCHAR(50) NOT NULL,
  number_of_hotels INT NOT NULL,
  PRIMARY KEY (chain_ID)
);

CREATE TABLE Hotel (
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

CREATE TABLE Employee (
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

CREATE TABLE Hotel_Phone_Number (
  hotel_ID INT,
  phone_number VARCHAR(20),
  PRIMARY KEY (hotel_ID, phone_number),
  FOREIGN KEY (hotel_ID) REFERENCES Hotel(hotel_ID)
);

CREATE TABLE Hotel_Chain_Central_Office_Address (
  chain_ID INT,
  address_street_name VARCHAR(50) NOT NULL,
  address_street_number INT NOT NULL,
  address_city VARCHAR(50) NOT NULL,
  address_province_state VARCHAR(50) NOT NULL,
  address_country VARCHAR(50) NOT NULL,
  PRIMARY KEY (chain_ID),
  FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
);

CREATE TABLE Hotel_Chain_Contact_Email (
  chain_ID INT,
  contact_email VARCHAR(50) NOT NULL,
  PRIMARY KEY (chain_ID),
  FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
);

CREATE TABLE Hotel_Chain_Phone_Number (
  chain_ID INT,
  phone_number VARCHAR(12),
  PRIMARY KEY (chain_ID, phone_number),
  FOREIGN KEY (chain_ID) REFERENCES Hotel_Chain(chain_ID)
);

CREATE TABLE Room (
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

CREATE TABLE Amenity (
  amenity_id INT,
  amenity_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (amenity_id)
);

CREATE TABLE Has_Amenity (
  amenity_id INT,
  hotel_id INT,
  room_number INT,
  PRIMARY KEY (amenity_id, hotel_id, room_number),
  FOREIGN KEY (hotel_id, room_number) REFERENCES Room(hotel_ID, room_number)
);

CREATE TABLE Customer (
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

CREATE TABLE Booking (
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

CREATE TABLE Rental (
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

CREATE TABLE Users (
    user_SSN_SIN INT PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(10) NOT NULL,
    CHECK (role = 'customer' OR role = 'employee')
);