import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { Container, Text, Box } from "@mantine/core";
import Room from "~/components/Room";
import Header from "~/components/Header";
import useSearchQuery from "~/utils/useSearchQuery";
import { HotelSearch } from "~/types";

const removeNullValues = (obj: any) => {
  const newObj: any = {};

  for (let key in obj) {
    if (!obj[key]) newObj[key] = obj[key];
  }

  return newObj;
};

export default function Home() {
  const {
    startDate,
    endDate,
    price,
    hotelChain,
    category,
    numberOfRooms,
    roomCapacity,
    location,
  } = useSearchQuery((state) => state);
  const debounceState = useRef<null | number>(null);
  const [result, setResult] = useState<HotelSearch[]>([]);

  useEffect(() => {
    if (debounceState.current != null) {
      clearTimeout(debounceState.current as number);
      debounceState.current = setTimeout(() => {
        debounceState.current = null;
      }, 1000) as any;
    }

    axios
      .get<HotelSearch[]>("http://127.0.0.1:5000/hotel/hotel/search", {
        params: removeNullValues({
          start_date: startDate,
          end_date: endDate,
          hotel_chain: hotelChain,
          city: location,
          star_rating: category,
          room_capacity: roomCapacity,
          price_per_night: price,
        }),
      })
      .then((res) => {
        setResult(res.data);
      });

    debounceState.current = setTimeout(() => {
      debounceState.current = null;
    }, 1000) as any;
  }, [
    startDate,
    endDate,
    price,
    hotelChain,
    category,
    numberOfRooms,
    roomCapacity,
    location,
  ]);

  return (
    <>
      <Header displayFilter />
      <main>
        <Container sx={{ marginTop: "20px" }}>
          {result.map((hotel) => (
            <Box key={hotel.hotel_id}>
              {hotel.rooms.map((room) => (
                <Room
                  key={`${room.room_number}-${room.hotel_id}`}
                  room={room}
                  hotel={hotel}
                />
              ))}
            </Box>
          ))}
          {result.length && (
            <Text>No rooms available with the given criteria</Text>
          )}
        </Container>
      </main>
    </>
  );
}
