INSERT INTO Customer (customer_SSN_SIN, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, registration_date)
VALUES
(123456789, 'John', 'Doe', '123 Main St', 10, 'Anytown', 'Anyprovince', 'Anycountry', '2020-01-01'),
(234567890, 'Jane', 'Doe', '456 Maple Ave', 20, 'Anycity', 'Anystate', 'Anycountry', '2020-02-01'),
(345678901, 'Bob', 'Smith', '789 Oak St', 30, 'Somecity', 'Someprovince', 'Somecountry', '2020-03-01'),
(456789012, 'Alice', 'Johnson', '1010 Elm St', 40, 'Anothercity', 'Anotherprovince', 'Anothercountry', '2020-04-01'),
(567890123, 'Sam', 'Lee', '1212 Cedar St', 50, 'Yetanothercity', 'Yetanotherprovince', 'Yetanothercountry', '2020-05-01'),
(678901234, 'Karen', 'Chen', '1414 Pine St', 60, 'Someothercity', 'Someotherprovince', 'Someothercountry', '2020-06-01'),
(789012345, 'David', 'Kim', '1616 Birch St', 70, 'Anadditionalcity', 'Anadditionalprovince', 'Anadditionalcountry', '2020-07-01'),
(890123456, 'Sarah', 'Davis', '1818 Walnut St', 80, 'Yetanotheradditionalcity', 'Yetanotheradditionalprovince', 'Yetanotheradditionalcountry', '2020-08-01'),
(901234567, 'Michael', 'Nguyen', '2020 Oakwood Dr', 90, 'Mycity', 'Myprovince', 'Mycountry', '2020-09-01'),
(123450987, 'Emily', 'Wang', '2222 Maplewood Dr', 100, 'Anothercity', 'Anotherprovince', 'Anothercountry', '2020-10-01');

INSERT INTO Booking (booking_ID, booking_date, scheduled_check_in_date, scheduled_check_out_date, canceled, customer_SSN_SIN, room_number, hotel_ID)
VALUES
(1, '2023-04-01', '2023-04-05', '2023-04-10', false, 123456789, 1, 103),
(2, '2023-04-02', '2023-04-07', '2023-04-12', false, 234567890, 2, 105),
(3, '2023-04-03', '2023-04-06', '2023-04-09', true, 345678901, 3, 201),
(4, '2023-04-04', '2023-04-10', '2023-04-15', false, 456789012, 4, 204),
(5, '2023-04-05', '2023-04-12', '2023-04-17', true, 567890123, 5, 302),
(6, '2023-04-06', '2023-04-15', '2023-04-20', false, 678901234, 1, 401),
(7, '2023-04-07', '2023-04-20', '2023-04-25', false, 789012345, 2, 502),
(8, '2023-04-08', '2023-04-25', '2023-04-30', false, 890123456, 3, 504),
(9, '2023-04-09', '2023-04-22', '2023-04-27', false, 901234567, 4, 506),
(10, '2023-04-10', '2023-04-28', '2023-05-03', false, 123450987, 5, 508);

INSERT INTO Rental (rental_ID, base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID, room_number, hotel_ID, employee_ID, employee_SSN_SIN)
VALUES
(1, 100, '2023-04-01', 100, 0, 0, '2023-04-05', '2023-04-10', 123456789, 1, 1, 103, 1, 111111111),
(2, 120, '2023-04-02', 120, 0, 0, '2023-04-07', '2023-04-12', 234567890, 2, 2, 105, 1, 111111111),
(3, 90, '2023-04-03', 90, 10, 20, '2023-04-06', '2023-04-09', 345678901, 3, 3, 201, 1, 111111111),
(4, 150, '2023-04-04', 150, 0, 0, '2023-04-10', '2023-04-15', 456789012, 4, 4, 204, 1, 111111111),
(5, 80, '2023-04-05', 80, 15, 10, '2023-04-12', '2023-04-17', 567890123, 5, 5, 302, 1, 111111111),
(6, 200, '2023-04-06', 200, 5, 0, '2023-04-15', '2023-04-20', 678901234, 6, 1, 401, 1, 111111111),
(7, 180, '2023-04-07', 180, 0, 0, '2023-04-20', '2023-04-25', 789012345, 7, 2, 502, 1, 111111111),
(8, 130, '2023-04-08', 130, 20, 30, '2023-04-25', '2023-04-30', 890123456, 8, 3, 504, 1, 111111111),
(9, 160, '2023-04-09', 160, 0, 0, '2023-04-22', '2023-04-27', 901234567, 9, 4, 506, 1, 111111111),
(10, 110, '2023-04-10', 110, 25, 15, '2023-04-28', '2023-05-03', 123450987, 10, 5, 508, 1, 111111111);

INSERT INTO Employee (employee_SSN_SIN, employee_ID, first_name, last_name, address_street_name, address_street_number, address_city, address_province_state, address_country, hotel_ID, is_manager)
VALUES
(111111111, 1, 'John', 'Doe', 'Main St', 123, 'Vancouver', 'BC', 'Canada', 103, true);


-- capacity of all the rooms of a specific hotel

create view hotel_total_room_capacity as
select hotel_id, room_number, room_capacity
from Room;

select * from hotel_total_room_capacity;

-- number of available rooms per area
create view available_rooms_in_area as
select count(*), address_country, address_province_state, address_city
from Room natural join Hotel
where (room_number, hotel_ID) not in ((select room_number, hotel_ID
                                    from rental where check_in_date > '2023-04-03' and check_out_date < '2023-04-25')
                                    union
                                    (select room_number, hotel_ID
                                    from booking where scheduled_check_in_date > '2023-04-03' and scheduled_check_out_date < '2023-04-25' and canceled = false))
group by address_country, address_province_state, address_city;

