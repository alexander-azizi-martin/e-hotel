-- Insert data for Hotel_Chain table
INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (1, 'Hilton', 8);
INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (2, 'Marriott International', 8);
INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (3, 'InterContinental Hotels Group', 8);
INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (4, 'AccorHotels', 8);
INSERT INTO Hotel_Chain (chain_ID, name, number_of_hotels) VALUES (5, 'Wyndham Hotels and Resorts', 8);

-- Insert data for Hotel_Chain_Central_Office_Address, Hotel_Chain_Contact_Email, and Hotel_Chain_Phone_Number tables
INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country)
VALUES (1, 'Park Ave', 123, 'New York', 'NY', 'USA');

INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country)
VALUES (2, 'Fern Ave', 456, 'Bethesda', 'MD', 'USA');

INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country)
VALUES (3, 'Park St', 789, 'Denham', 'Buckinghamshire', 'England');

INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country)
VALUES (4, 'Rue de la Boétie', 159, 'Paris', 'Île-de-France', 'France');

INSERT INTO Hotel_Chain_Central_Office_Address (chain_ID, address_street_name, address_street_number, address_city, address_province_state, address_country)
VALUES (5, 'Broadway', 456, 'New York', 'NY', 'USA');

INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (1, 'info@hilton.com');
INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (1, '555-123-4567');

INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (2, 'info@marriott.com');
INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (2, '555-234-5678');

INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (3, 'info@ihg.com');
INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (3, '555-345-6789');

INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (4, 'info@accorhotels.com');
INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (4, '555-456-7890');

INSERT INTO Hotel_Chain_Contact_Email (chain_ID, contact_email) VALUES (5, 'info@wyndham.com');
INSERT INTO Hotel_Chain_Phone_Number (chain_ID, phone_number) VALUES (5, '555-567-8901');

-- Insert hotels
-- Insert data for Hilton hotel chain
-- Hilton
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (101, 200, 'Main St', 123, 'New York', 'NY', 'USA', 'hilton1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (102, 250, 'Market St', 456, 'San Francisco', 'CA', 'USA', 'hilton2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (103, 300, 'Baker St', 789, 'London', 'England', 'UK', 'hilton3@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (104, 220, 'King St', 321, 'Toronto', 'ON', 'Canada', 'hilton4@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (105, 280, 'George St', 654, 'Sydney', 'NSW', 'Australia', 'hilton5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (106, 240, 'Queen St', 987, 'Auckland', 'Auckland', 'New Zealand', 'hilton6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (107, 260, 'Orchard Rd', 135, 'Singapore', 'Singapore', 'Singapore', 'hilton7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (108, 230, 'Las Ramblas', 246, 'Barcelona', 'Catalonia', 'Spain', 'hilton8@example.com', 4);

-- Marriott 
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (201, 300, 'Madison Ave', 369, 'New York', 'NY', 'USA', 'marriott1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (202, 320, 'Mission St', 482, 'San Francisco', 'CA', 'USA', 'marriott2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (203, 350, 'Oxford St', 793, 'London', 'England', 'UK', 'marriott3@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (204, 270, 'Front St', 345, 'Toronto', 'ON', 'Canada', 'marriott4@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (205, 330, 'Pitt St', 678, 'Sydney', 'NSW', 'Australia', 'marriott5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (206, 290, 'Victoria St', 951, 'Auckland', 'Auckland', 'New Zealand', 'marriott6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (207, 310, 'Shenton Way', 147, 'Singapore', 'Singapore', 'Singapore', 'marriott7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (208, 280, 'Passeig de Gracia', 258, 'Barcelona', 'Catalonia', 'Spain', 'marriott8@example.com', 4);

-- Intercontinental 
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (301, 250, 'Park Ave', 159, 'New York', 'NY', 'USA', 'intercontinental1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (302, 270, 'Van Ness Ave', 498, 'San Francisco', 'CA', 'USA', 'intercontinental2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (303, 320, 'Regent St', 777, 'London', 'England', 'UK', 'intercontinental3@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (304, 260, 'Yonge St', 369, 'Toronto', 'ON', 'Canada', 'intercontinental4@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (305, 280, 'Elizabeth St', 702, 'Sydney', 'NSW', 'Australia', 'intercontinental5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (306, 300, 'Wellesley St', 915, 'Auckland', 'Auckland', 'New Zealand', 'intercontinental6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (307, 280, 'Bukit Timah Rd', 741, 'Singapore', 'Singapore', 'Singapore', 'intercontinental7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (308, 310, 'Passeig de Gracia', 369, 'Barcelona', 'Catalonia', 'Spain', 'intercontinental8@example.com', 4);

-- AccorHotels
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (401, 280, 'Fifth Ave', 963, 'New York', 'NY', 'USA', 'accor1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (402, 300, 'Geary St', 456, 'San Francisco', 'CA', 'USA', 'accor2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (403, 320, 'Coventry St', 678, 'London', 'England', 'UK', 'accor3@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (404, 240, 'Queen St', 123, 'Toronto', 'ON', 'Canada', 'accor4@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (405, 290, 'Pitt St', 456, 'Sydney', 'NSW', 'Australia', 'accor5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (406, 250, 'Albert St', 789, 'Auckland', 'Auckland', 'New Zealand', 'accor6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (407, 270, 'Cecil St', 369, 'Singapore', 'Singapore', 'Singapore', 'accor7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (408, 260, 'Rambla de Catalunya', 159, 'Barcelona', 'Catalonia', 'Spain', 'accor8@example.com', 4);

--Wyndham
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (501, 320, 'Broadway', 789, 'New York', 'NY', 'USA', 'wyndham1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (502, 300, 'Fisherman''s Wharf', 456, 'San Francisco', 'CA', 'USA', 'wyndham2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (503, 350, 'Baker St', 852, 'London', 'England', 'UK', 'wyndham3@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (504, 240, 'Queen St', 654, 'Toronto', 'ON', 'Canada', 'wyndham4@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (505, 280, 'George St', 147, 'Sydney', 'NSW', 'Australia', 'wyndham5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (506, 260, 'Queen St', 369, 'Auckland', 'Auckland', 'New Zealand', 'wyndham6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (507, 290, 'Orchard Rd', 951, 'Singapore', 'Singapore', 'Singapore', 'wyndham7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (508, 270, 'Passeig de Gracia', 753, 'Barcelona', 'Catalonia', 'Spain', 'wyndham8@example.com', 4);

-- Hotel phone numbers
-- Hilton
-- Hilton Hotel Phone Numbers
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (101, '+1-555-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (102, '+1-555-2345');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (103, '+44-20-1234-5678');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (104, '+1-416-555-6789');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (105, '+61-2-555-7890');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (106, '+64-9-555-8901');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (107, '+65-6222-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (108, '+34-93-567-8901');

-- Marriott Hotel Phone Numbers
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (201, '+1-212-555-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (202, '+1-415-555-2345');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (203, '+44-20-1234-5678');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (204, '+1-416-555-6789');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (205, '+61-2-555-7890');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (206, '+64-9-555-8901');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (207, '+65-6222-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (208, '+34-93-567-8901');

-- Intercontinental Hotel Phone Numbers
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (301, '+1-212-555-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (302, '+1-415-555-2345');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (303, '+44-20-1234-5678');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (304, '+1-416-555-6789');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (305, '+61-2-555-7890');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (306, '+64-9-555-8901');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (307, '+65-6222-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (308, '+34-93-567-8901');

-- AccorHotels Phone Numbers
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (401, '+1-212-555-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (402, '+1-415-555-2345');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (403, '+44-20-1234-5678');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (404, '+1-416-555-6789');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (405, '+61-2-555-7890');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (406, '+64-9-555-8901');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (407, '+65-6222-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (408, '+34-93-567-8901');

-- Wyndham Phone Numbers
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (501, '+1-212-555-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (502, '+1-415-555-2345');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (503, '+44-20-1234-5678');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (504, '+1-416-555-6789');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (505, '+61-2-555-7890');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (506, '+64-9-555-8901');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (507, '+65-6222-1234');
INSERT INTO Hotel_Phone_Number (hotel_ID, phone_number) VALUES (508, '+34-93-567-8901');

-- Rooms
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (1, 101, 1, 'City', 100, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (2, 101, 2, 'City', 150, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (3, 101, 3, 'City', 200, FALSE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (4, 101, 4, 'City', 250, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (5, 101, 5, 'City', 300, FALSE, NULL);

-- Hilton 2
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (1, 102, 1, 'City', 100, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (2, 102, 2, 'City', 150, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (3, 102, 3, 'City', 200, FALSE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (4, 102, 4, 'City', 250, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (5, 102, 5, 'City', 300, FALSE, NULL);

-- Hilton 3
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (1, 103, 1, 'City', 100, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (2, 103, 2, 'Garden', 150, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (3, 103, 3, 'Garden', 200, FALSE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (4, 103, 4, 'City', 250, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (5, 103, 5, 'City', 300, FALSE, NULL); 

-- Hilton 4
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (1, 104, 1, 'City', 100, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (2, 104, 2, 'Garden', 150, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (3, 104, 3, 'Garden', 200, FALSE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (4, 103, 4, 'City', 250, TRUE, NULL);
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES (5, 103, 5, 'City', 300, FALSE, NULL); 









