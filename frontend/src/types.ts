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