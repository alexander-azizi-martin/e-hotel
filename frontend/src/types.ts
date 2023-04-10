export interface Token {
    user_ssn_sin: string;
    first_name: string;
    last_name: string;
    role: string;
}

export interface RoomInfo {
    room_number: number;
    hotel_id: number;
    room_capacity: number;
    view_type: string;
    price_per_night: number;
    is_extendable: boolean;
    room_problems: string;
}

export interface BookingInfo {
    booking_ID: number;
    booking_date: string;
    scheduled_check_in_date: string;
    scheduled_check_out_date: string;
    canceled: boolean;
    customer_SSN_SIN: number;
    room_number: number;
    hotel_ID: number;
}

export interface HotelChainInfo {
    chain_ID: number;
    name: string;
    number_of_hotels: number;
}