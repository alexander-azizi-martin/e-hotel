DO $$
DECLARE
    booking_ID_input INTEGER := 3;
    base_price INTEGER := 123;
    date_paid DATE := '2023-04-01';
    total_paid INTEGER := 123;
    discount INTEGER := 123;
    additional_charges INTEGER := 0;
    employee_ID INTEGER := 1;
    employee_SSN_SIN INTEGER := 111111111;

BEGIN
    -- Use the variables in a query
    insert into rental(base_price, date_paid, total_paid, discount, additional_charges, check_in_date, check_out_date, customer_SSN_SIN, booking_ID,
                       room_number, hotel_ID, employee_ID, employee_SSN_SIN)
    (select base_price, date_paid, total_paid, discount, additional_charges, scheduled_check_in_date, scheduled_check_out_date, customer_SSN_SIN, booking_ID,
            room_number, hotel_ID, employee_ID, employee_SSN_SIN
    from booking
    where booking_ID = booking_ID_input);

END $$;
