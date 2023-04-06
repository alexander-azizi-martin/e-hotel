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
INSERT INTO Hotel
    (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating)
VALUES
    (101, 1, 200, 'Main St', 123, 'New York', 'NY', 'USA', 'hilton1@example.com', 5),
    (102, 1, 250, 'Market St', 456, 'San Francisco', 'CA', 'USA', 'hilton2@example.com', 5),
    (103, 1, 300, 'Baker St', 789, 'London', 'England', 'UK', 'hilton3@example.com', 3),
    (104, 1, 220, 'King St', 321, 'Toronto', 'ON', 'Canada', 'hilton4@example.com', 4),
    (105, 1, 280, 'George St', 654, 'Sydney', 'NSW', 'Australia', 'hilton5@example.com', 5),
    (106, 1, 240, 'Queen St', 987, 'Auckland', 'Auckland', 'New Zealand', 'hilton6@example.com', 2),
    (107, 1, 260, 'Orchard Rd', 135, 'Singapore', 'Singapore', 'Singapore', 'hilton7@example.com', 5),
    (108, 1, 230, 'Las Ramblas', 246, 'Barcelona', 'Catalonia', 'Spain', 'hilton8@example.com', 4);


/* INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (101, 1, 200, 'Main St', 123, 'New York', 'NY', 'USA', 'hilton1@example.com', 5);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (102, 1, 250, 'Market St', 456, 'San Francisco', 'CA', 'USA', 'hilton2@example.com', 5);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (103, 1, 300, 'Baker St', 789, 'London', 'England', 'UK', 'hilton3@example.com', 3);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (104, 1, 220, 'King St', 321, 'Toronto', 'ON', 'Canada', 'hilton4@example.com', 4);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (105, 1, 280, 'George St', 654, 'Sydney', 'NSW', 'Australia', 'hilton5@example.com', 5);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (106, 1, 240, 'Queen St', 987, 'Auckland', 'Auckland', 'New Zealand', 'hilton6@example.com', 2);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (107, 1, 260, 'Orchard Rd', 135, 'Singapore', 'Singapore', 'Singapore', 'hilton7@example.com', 5);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (108, 1, 230, 'Las Ramblas', 246, 'Barcelona', 'Catalonia', 'Spain', 'hilton8@example.com', 4);
*/
-- Marriott 
INSERT INTO Hotel
    (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating)
VALUES
    (201, 2, 300, 'Madison Ave', 369, 'New York', 'NY', 'USA', 'marriott1@example.com', 5),
    (202, 2, 320, 'Mission St', 482, 'San Francisco', 'CA', 'USA', 'marriott2@example.com', 5),
    (203, 2, 350, 'Oxford St', 793, 'London', 'England', 'UK', 'marriott3@example.com', 3),
    (204, 2, 270, 'Front St', 345, 'Toronto', 'ON', 'Canada', 'marriott4@example.com', 4),
    (205, 2, 330, 'Pitt St', 678, 'Sydney', 'NSW', 'Australia', 'marriott5@example.com', 5),
    (206, 2, 290, 'Victoria St', 951, 'Auckland', 'Auckland', 'New Zealand', 'marriott6@example.com', 2),
    (207, 2, 310, 'Shenton Way', 147, 'Singapore', 'Singapore', 'Singapore', 'marriott7@example.com', 5),
    (208, 2, 280, 'Passeig de Gracia', 258, 'Barcelona', 'Catalonia', 'Spain', 'marriott8@example.com', 4);
/*
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (201, 300, 'Madison Ave', 369, 'New York', 'NY', 'USA', 'marriott1@example.com', 5);
INSERT INTO Hotel (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (202, 320, 'Mission St', 482, 'San Francisco', 'CA', 'USA', 'marriott2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (203, 350, 'Oxford St', 793, 'London', 'England', 'UK', 'marriott3@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (204, 270, 'Front St', 345, 'Toronto', 'ON', 'Canada', 'marriott4@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (205, 330, 'Pitt St', 678, 'Sydney', 'NSW', 'Australia', 'marriott5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (206, 290, 'Victoria St', 951, 'Auckland', 'Auckland', 'New Zealand', 'marriott6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (207, 310, 'Shenton Way', 147, 'Singapore', 'Singapore', 'Singapore', 'marriott7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (208, 280, 'Passeig de Gracia', 258, 'Barcelona', 'Catalonia', 'Spain', 'marriott8@example.com', 4);
*/
-- Intercontinental 
INSERT INTO Hotel
    (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating)
VALUES
    (301, 3, 250, 'Park Ave', 159, 'New York', 'NY', 'USA', 'intercontinental1@example.com', 5),
    (302, 3, 270, 'Van Ness Ave', 498, 'San Francisco', 'CA', 'USA', 'intercontinental2@example.com', 5),
    (303, 3, 320, 'Regent St', 777, 'London', 'England', 'UK', 'intercontinental3@example.com', 3),
    (304, 3, 260, 'Yonge St', 369, 'Toronto', 'ON', 'Canada', 'intercontinental4@example.com', 4),
    (305, 3, 280, 'Elizabeth St', 702, 'Sydney', 'NSW', 'Australia', 'intercontinental5@example.com', 5),
    (306, 3, 300, 'Wellesley St', 915, 'Auckland', 'Auckland', 'New Zealand', 'intercontinental6@example.com', 2),
    (307, 3, 280, 'Bukit Timah Rd', 741, 'Singapore', 'Singapore', 'Singapore', 'intercontinental7@example.com', 5),
    (308, 3, 310, 'Passeig de Gracia', 369, 'Barcelona', 'Catalonia', 'Spain', 'intercontinental8@example.com', 4);
/*
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (301, 250, 'Park Ave', 159, 'New York', 'NY', 'USA', 'intercontinental1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (302, 270, 'Van Ness Ave', 498, 'San Francisco', 'CA', 'USA', 'intercontinental2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (303, 320, 'Regent St', 777, 'London', 'England', 'UK', 'intercontinental3@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (304, 260, 'Yonge St', 369, 'Toronto', 'ON', 'Canada', 'intercontinental4@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (305, 280, 'Elizabeth St', 702, 'Sydney', 'NSW', 'Australia', 'intercontinental5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (306, 300, 'Wellesley St', 915, 'Auckland', 'Auckland', 'New Zealand', 'intercontinental6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (307, 280, 'Bukit Timah Rd', 741, 'Singapore', 'Singapore', 'Singapore', 'intercontinental7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (308, 310, 'Passeig de Gracia', 369, 'Barcelona', 'Catalonia', 'Spain', 'intercontinental8@example.com', 4);
*/
-- AccorHotels
INSERT INTO Hotel
    (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating)
VALUES
    (401, 4, 280, 'Fifth Ave', 963, 'New York', 'NY', 'USA', 'accor1@example.com', 5),
    (402, 4, 300, 'Geary St', 456, 'San Francisco', 'CA', 'USA', 'accor2@example.com', 5),
    (403, 4, 320, 'Coventry St', 678, 'London', 'England', 'UK', 'accor3@example.com', 4),
    (404, 4, 240, 'Queen St', 123, 'Toronto', 'ON', 'Canada', 'accor4@example.com', 3),
    (405, 4, 290, 'Pitt St', 456, 'Sydney', 'NSW', 'Australia', 'accor5@example.com', 5),
    (406, 4, 250, 'Albert St', 789, 'Auckland', 'Auckland', 'New Zealand', 'accor6@example.com', 2),
    (407, 4, 270, 'Cecil St', 369, 'Singapore', 'Singapore', 'Singapore', 'accor7@example.com', 5),
    (408, 4, 260, 'Rambla de Catalunya', 159, 'Barcelona', 'Catalonia', 'Spain', 'accor8@example.com', 4);
/*
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (401, 280, 'Fifth Ave', 963, 'New York', 'NY', 'USA', 'accor1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (402, 300, 'Geary St', 456, 'San Francisco', 'CA', 'USA', 'accor2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (403, 320, 'Coventry St', 678, 'London', 'England', 'UK', 'accor3@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (404, 240, 'Queen St', 123, 'Toronto', 'ON', 'Canada', 'accor4@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (405, 290, 'Pitt St', 456, 'Sydney', 'NSW', 'Australia', 'accor5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (406, 250, 'Albert St', 789, 'Auckland', 'Auckland', 'New Zealand', 'accor6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (407, 270, 'Cecil St', 369, 'Singapore', 'Singapore', 'Singapore', 'accor7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (408, 260, 'Rambla de Catalunya', 159, 'Barcelona', 'Catalonia', 'Spain', 'accor8@example.com', 4);
*/
--Wyndham
INSERT INTO Hotel
    (hotel_ID, chain_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating)
VALUES
    (501, 5, 320, 'Broadway', 789, 'New York', 'NY', 'USA', 'wyndham1@example.com', 5),
    (502, 5, 300, 'Fisherman''s Wharf', 456, 'San Francisco', 'CA', 'USA', 'wyndham2@example.com', 5),
    (503, 5, 350, 'Baker St', 852, 'London', 'England', 'UK', 'wyndham3@example.com', 4),
    (504, 5, 240, 'Queen St', 654, 'Toronto', 'ON', 'Canada', 'wyndham4@example.com', 3),
    (505, 5, 280, 'George St', 147, 'Sydney', 'NSW', 'Australia', 'wyndham5@example.com', 5),
    (506, 5, 260, 'Queen St', 369, 'Auckland', 'Auckland', 'New Zealand', 'wyndham6@example.com', 2),
    (507, 5, 290, 'Orchard Rd', 951, 'Singapore', 'Singapore', 'Singapore', 'wyndham7@example.com', 5),
    (508, 5, 270, 'Passeig de Gracia', 753, 'Barcelona', 'Catalonia', 'Spain', 'wyndham8@example.com', 4);

/*
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (501, 320, 'Broadway', 789, 'New York', 'NY', 'USA', 'wyndham1@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (502, 300, 'Fisherman''s Wharf', 456, 'San Francisco', 'CA', 'USA', 'wyndham2@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (503, 350, 'Baker St', 852, 'London', 'England', 'UK', 'wyndham3@example.com', 4);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (504, 240, 'Queen St', 654, 'Toronto', 'ON', 'Canada', 'wyndham4@example.com', 3);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (505, 280, 'George St', 147, 'Sydney', 'NSW', 'Australia', 'wyndham5@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (506, 260, 'Queen St', 369, 'Auckland', 'Auckland', 'New Zealand', 'wyndham6@example.com', 2);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (507, 290, 'Orchard Rd', 951, 'Singapore', 'Singapore', 'Singapore', 'wyndham7@example.com', 5);
INSERT INTO Hotel (hotel_ID, number_of_rooms, address_street_name, address_street_number, address_city, address_province_state, address_country, contact_email, star_rating) VALUES (508, 270, 'Passeig de Gracia', 753, 'Barcelona', 'Catalonia', 'Spain', 'wyndham8@example.com', 4);
*/
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
-- Hotel 103 (5-star)
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 103, 2, 'City', 300, TRUE, NULL),
       (2, 103, 2, 'Garden', 320, TRUE, NULL),
       (3, 103, 3, 'Pool', 350, FALSE, NULL),
       (4, 103, 4, 'City', 400, TRUE, NULL),
       (5, 103, 4, 'Garden', 420, FALSE, NULL);

-- Hotel 104 (5-star)
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 104, 2, 'City', 320, TRUE, NULL),
       (2, 104, 3, 'Garden', 360, TRUE, NULL),
       (3, 104, 3, 'Pool', 380, FALSE, NULL),
       (4, 104, 4, 'City', 420, TRUE, NULL),
       (5, 104, 5, 'Garden', 500, FALSE, NULL);

-- Hotel 105 (3-star)
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 105, 1, 'City', 100, TRUE, NULL),
       (2, 105, 2, 'Garden', 150, TRUE, NULL),
       (3, 105, 2, 'Pool', 170, FALSE, NULL),
       (4, 105, 3, 'City', 200, TRUE, NULL),
       (5, 105, 3, 'Garden', 220, FALSE, NULL);

-- Hotel 106 (4-star)
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 106, 2, 'City', 250, TRUE, NULL),
       (2, 106, 3, 'Garden', 290, TRUE, NULL),
       (3, 106, 3, 'Pool', 320, FALSE, NULL),
       (4, 106, 4, 'City', 380, TRUE, NULL),
       (5, 106, 5, 'Garden', 450, FALSE, NULL);

-- Hotel 107 (5-star)
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 107, 2, 'City', 320, TRUE, NULL),
       (2, 107, 2, 'Garden', 350, TRUE, NULL),
       (3, 107, 3, 'Pool', 400, FALSE, NULL),
       (4, 107, 4, 'City', 450, TRUE, NULL),
       (5, 107, 4, 'Garden', 500, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 108, 1, 'City', 75, TRUE, NULL),
(2, 108, 2, 'Pool', 125, TRUE, NULL),
(3, 108, 2, 'Garden', 125, TRUE, NULL),
(4, 108, 3, 'City', 175, TRUE, NULL),
(5, 108, 4, 'Pool', 225, FALSE, NULL);

-- Hotel 201
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 201, 1, 'City', 50, TRUE, NULL),
(2, 201, 2, 'Garden', 100, TRUE, NULL),
(3, 201, 2, 'Pool', 100, TRUE, NULL),
(4, 201, 3, 'City', 150, TRUE, NULL),
(5, 201, 4, 'Garden', 200, FALSE, NULL);

-- Hotel 202
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 202, 1, 'City', 55, TRUE, NULL),
(2, 202, 2, 'Garden', 110, TRUE, NULL),
(3, 202, 2, 'Pool', 110, TRUE, NULL),
(4, 202, 3, 'City', 165, TRUE, NULL),
(5, 202, 4, 'Garden', 220, FALSE, NULL);

-- Hotel 203
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 203, 1, 'City', 45, TRUE, NULL),
(2, 203, 2, 'Garden', 90, TRUE, NULL),
(3, 203, 2, 'Pool', 90, TRUE, NULL),
(4, 203, 3, 'City', 135, TRUE, NULL),
(5, 203, 4, 'Garden', 180, FALSE, NULL);

-- Hotel 204
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 204, 1, 'City', 60, TRUE, NULL),
(2, 204, 2, 'Garden', 120, TRUE, NULL),
(3, 204, 2, 'Pool', 120, TRUE, NULL),
(4, 204, 3, 'City', 180, TRUE, NULL),
(5, 204, 4, 'Garden', 240, FALSE, NULL);

-- Hotel 205
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 205, 1, 'City', 75, TRUE, NULL),
(2, 205, 2, 'Garden', 150, TRUE, NULL),
(3, 205, 2, 'Pool', 150, TRUE, NULL),
(4, 205, 3, 'City', 225, TRUE, NULL),
(5, 205, 4, 'Garden', 300, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 206, 2, 'City', 120, TRUE, NULL),
(2, 206, 4, 'Garden', 220, TRUE, NULL),
(3, 206, 3, 'Pool', 180, FALSE, 'Leaky faucet'),
(4, 206, 2, 'City', 120, FALSE, NULL),
(5, 206, 1, 'City', 100, TRUE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 207, 3, 'Garden', 210, TRUE, NULL),
(2, 207, 2, 'City', 140, TRUE, NULL),
(3, 207, 4, 'Pool', 240, FALSE, 'Broken AC'),
(4, 207, 1, 'City', 90, FALSE, 'No hot water'),
(5, 207, 2, 'Garden', 160, TRUE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 208, 5, 'Pool', 350, TRUE, 'Stained carpet'),
(2, 208, 2, 'City', 140, TRUE, NULL),
(3, 208, 3, 'Garden', 210, FALSE, NULL),
(4, 208, 4, 'Pool', 280, TRUE, NULL),
(5, 208, 1, 'City', 90, TRUE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 301, 4, 'Garden', 280, TRUE, 'Clogged sink'),
(2, 301, 2, 'City', 140, TRUE, NULL),
(3, 301, 3, 'Pool', 210, FALSE, NULL),
(4, 301, 5, 'Pool', 350, TRUE, NULL),
(5, 301, 1, 'City', 90, TRUE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 302, 3, 'Garden', 210, TRUE, NULL),
(2, 302, 2, 'City', 140, TRUE, NULL),
(3, 302, 4, 'Pool', 280, FALSE, 'Leaky shower'),
(4, 302, 1, 'City', 90, FALSE, NULL),
(5, 302, 2, 'Garden', 160, TRUE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 303, 1, 'City', 100, TRUE, NULL),
(2, 303, 2, 'City', 140, TRUE, NULL),
(3, 303, 3, 'Pool', 210, FALSE, 'Noisy AC'),
(4, 303, 4, 'Garden', 280, TRUE, NULL),
(5, 303, 5, 'Pool', 350, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
(1, 304, 2, 'City', 140, TRUE, NULL),
(2, 304, 4, 'Pool', 280, TRUE, NULL),
(3, 304, 1, 'City', 90, FALSE, NULL),
(4, 304, 3, 'Garden', 210, TRUE, NULL),
(5, 304, 5, 'Pool', 350, FALSE, 'Broken TV');

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 305, 1, 'City', 50, TRUE, NULL),
       (2, 305, 2, 'Garden', 75, TRUE, NULL),
       (3, 305, 3, 'Pool', 100, FALSE, NULL),
       (4, 305, 4, 'City', 125, TRUE, NULL),
       (5, 305, 5, 'Garden', 150, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 306, 1, 'Pool', 50, TRUE, NULL),
       (2, 306, 2, 'City', 75, TRUE, NULL),
       (3, 306, 3, 'Garden', 100, FALSE, NULL),
       (4, 306, 4, 'Pool', 125, TRUE, NULL),
       (5, 306, 5, 'City', 150, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 307, 1, 'Garden', 50, TRUE, NULL),
       (2, 307, 2, 'Pool', 75, TRUE, NULL),
       (3, 307, 3, 'City', 100, FALSE, NULL),
       (4, 307, 4, 'Garden', 125, TRUE, NULL),
       (5, 307, 5, 'Pool', 150, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 308, 1, 'City', 50, TRUE, NULL),
       (2, 308, 2, 'Garden', 75, TRUE, NULL),
       (3, 308, 3, 'Pool', 100, FALSE, NULL),
       (4, 308, 4, 'City', 125, TRUE, NULL),
       (5, 308, 5, 'Garden', 150, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 401, 1, 'Pool', 50, TRUE, NULL),
       (2, 401, 2, 'City', 75, TRUE, NULL),
       (3, 401, 3, 'Garden', 100, FALSE, NULL),
       (4, 401, 4, 'Pool', 125, TRUE, NULL),
       (5, 401, 5, 'City', 150, FALSE, NULL);

-- Hotel 402
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 402, 2, 'City', 80, TRUE, NULL),
       (2, 402, 4, 'Garden', 150, TRUE, NULL),
       (3, 402, 2, 'Pool', 100, TRUE, 'Leaky faucet'),
       (4, 402, 1, 'City', 60, FALSE, NULL),
       (5, 402, 3, 'Garden', 120, TRUE, NULL);

-- Hotel 403
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 403, 1, 'City', 70, FALSE, 'Broken AC'),
       (2, 403, 2, 'Pool', 120, TRUE, NULL),
       (3, 403, 3, 'Garden', 160, TRUE, NULL),
       (4, 403, 2, 'City', 100, TRUE, NULL),
       (5, 403, 4, 'Garden', 200, TRUE, 'Clogged toilet');

-- Hotel 404
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 404, 1, 'City', 50, FALSE, NULL),
       (2, 404, 2, 'Garden', 90, TRUE, NULL),
       (3, 404, 3, 'City', 130, TRUE, NULL),
       (4, 404, 4, 'Pool', 180, TRUE, NULL),
       (5, 404, 5, 'Garden', 250, TRUE, NULL);

-- Hotel 405
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 405, 1, 'City', 60, FALSE, NULL),
       (2, 405, 2, 'Pool', 120, TRUE, 'TV not working'),
       (3, 405, 3, 'Garden', 160, TRUE, NULL),
       (4, 405, 2, 'City', 100, TRUE, NULL),
       (5, 405, 4, 'Garden', 200, TRUE, 'Leaky shower');

-- Hotel 406
INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 406, 1, 'City', 70, FALSE, NULL),
       (2, 406, 2, 'Garden', 120, TRUE, 'Broken hair dryer'),
       (3, 406, 3, 'City', 160, TRUE, NULL),
       (4, 406, 4, 'Pool', 200, TRUE, NULL),
       (5, 406, 5, 'Garden', 270, TRUE, 'Clogged sink');

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 407, 1, 'Garden', 75, TRUE, NULL),
(2, 407, 2, 'Pool', 100, TRUE, NULL),
(3, 407, 2, 'Garden', 100, FALSE, NULL),
(4, 407, 3, 'Pool', 150, TRUE, NULL),
(5, 407, 4, 'City', 200, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES (1, 408, 1, 'City', 75, TRUE, NULL),
(2, 408, 2, 'Garden', 100, TRUE, NULL),
(3, 408, 2, 'Pool', 100, FALSE, NULL),
(4, 408, 3, 'Garden', 150, TRUE, NULL),
(5, 408, 4, 'City', 200, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES
(1, 501, 1, 'Garden', 75, TRUE, NULL),
(2, 501, 2, 'City', 100, TRUE, NULL),
(3, 501, 2, 'Garden', 100, FALSE, NULL),
(4, 501, 3, 'City', 150, TRUE, NULL),
(5, 501, 4, 'Pool', 200, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES
(1, 502, 1, 'Pool', 75, TRUE, NULL),
(2, 502, 2, 'City', 100, TRUE, NULL),
(3, 502, 2, 'Garden', 100, FALSE, NULL),
(4, 502, 3, 'City', 150, TRUE, NULL),
(5, 502, 4, 'Pool', 200, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES
(1, 503, 1, 'Garden', 50, TRUE, NULL),
(2, 503, 2, 'City', 75, TRUE, NULL),
(3, 503, 2, 'Garden', 75, FALSE, NULL),
(4, 503, 3, 'Pool', 125, TRUE, NULL),
(5, 503, 4, 'City', 175, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES
(1, 504, 1, 'City', 50, TRUE, NULL),
(2, 504, 2, 'Garden', 75, TRUE, NULL),
(3, 504, 2, 'Pool', 75, FALSE, NULL),
(4, 504, 3, 'City', 125, TRUE, NULL),
(5, 504, 4, 'Garden', 175, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems) VALUES
(1, 505, 1, 'Pool', 50, TRUE, NULL),
(2, 505, 2, 'Garden', 75, TRUE, NULL),
(3, 505, 2, 'City', 75, FALSE, NULL),
(4, 505, 3, 'Garden', 125, TRUE, NULL),
(5, 505, 4, 'Pool', 175, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
    (1, 506, 1, 'City', 60, FALSE, NULL),
    (2, 506, 2, 'City', 80, TRUE, NULL),
    (3, 506, 2, 'Garden', 100, TRUE, NULL),
    (4, 506, 4, 'Garden', 160, TRUE, NULL),
    (5, 506, 4, 'Pool', 200, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
    (1, 507, 2, 'City', 120, TRUE, NULL),
    (2, 507, 2, 'Garden', 140, FALSE, NULL),
    (3, 507, 3, 'Garden', 180, TRUE, NULL),
    (4, 507, 4, 'Pool', 240, TRUE, NULL),
    (5, 507, 5, 'Pool', 300, FALSE, NULL);

INSERT INTO Room (room_number, hotel_ID, room_capacity, view_type, price_per_night, is_extendable, room_problems)
VALUES
    (1, 508, 1, 'City', 70, FALSE, NULL),
    (2, 508, 2, 'City', 100, TRUE, NULL),
    (3, 508, 3, 'Garden', 150, TRUE, NULL),
    (4, 508, 4, 'Pool', 220, TRUE, NULL),
    (5, 508, 5, 'Pool', 300, FALSE, NULL);

-- capacity of all the rooms of a specific hotel

create view hotel_total_room_capacity as
select room_number, room_capacity
from Room where hotel_ID = 103;

-- number of available rooms per area
create view available_rooms_in_area as
select count(*) as available_rooms
from Room natural join Hotel
where (room_number, hotel_ID) not in ((select room_number, hotel_ID
                                    from rental where check_in_date > '2023-04-03' and check_out_date < '2023-04-25')
                                    union
                                    (select room_number, hotel_ID
                                    from booking where scheduled_check_in_date > '2023-04-03' and scheduled_check_out_date < '2023-04-25' and canceled = false))
                                and address_country = 'USA' and address_province_state <> 'FL' and address_city <> 'UNFOUOUHFOGUHFHGU';


