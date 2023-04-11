import axios from "axios";
import dayjs from "dayjs";
import { useEffect, useRef, useState } from "react";
import { Container, Text, Box, Center, Loader } from "@mantine/core";
import Room from "~/components/Room";
import Header from "~/components/Header";
import useSearchQuery from "~/utils/useSearchQuery";
import { HotelChainSearch } from "~/types";

const formatParameters = (obj: any) => {
  const newObj: any = {};

  for (let key in obj) {
    if (obj[key]) {
      if (key === "room_capacity") {
        if (obj[key] === "any") continue;
        else newObj[key] = parseInt(obj[key]);
      } else {
        newObj[key] = obj[key];
      }
    }
  }

  if (!("start_date" in newObj)) {
    newObj["start_date"] = dayjs().subtract(5, "years").format("YYYY-MM-DD");
  }
  if (!("end_date" in newObj)) {
    newObj["end_date"] = dayjs().add(5, "years").format("YYYY-MM-DD");
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
  const [result, setResult] = useState<HotelChainSearch[]>([]);
  const [loading, setLoading] = useState(true);
  const firstRender = useRef(true);

  useEffect(() => {
    if (debounceState.current != null) {
      clearTimeout(debounceState.current as number);
    }

    debounceState.current = setTimeout(() => {
      setLoading(true);

      axios
        .get<HotelChainSearch[]>("http://127.0.0.1:5000/hotel/hotel/search", {
          params: formatParameters({
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
          firstRender.current = false;
          setLoading(false);
          setResult(res.data);
        });

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
          <Center>
            {result.map((hotelChain) => (
              <Box key={hotelChain.chain_ID}>
                {hotelChain.hotels.map((hotel) => (
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
              </Box>
            ))}
            {result.length === 0 && !loading && (
              <Text>No rooms available with the given criteria</Text>
            )}
            {firstRender.current && <Loader />}
          </Center>
        </Container>
      </main>
    </>
  );
}
