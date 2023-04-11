import axios from "axios";
import dayjs from "dayjs";
import { useEffect, useRef, useState } from "react";
import { Container, Text, Box, Center, Loader } from "@mantine/core";
import Room from "~/components/Room";
import Header from "~/components/Header";
import useSearchQuery from "~/utils/useSearchQuery";

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
  const [result, setResult] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const firstRender = useRef(true);

  useEffect(() => {
    if (debounceState.current != null) {
      clearTimeout(debounceState.current as number);
    }

    debounceState.current = setTimeout(() => {
      setLoading(true);

      axios.get<any[]>("http://127.0.0.1:5000/room/room").then((res) => {
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
            {result.map((room) => (
              <Box key={`${room.room_number}-${room.hotel_id}`}>
                <Room
                  key={`${room.room_number}-${room.hotel_id}`}
                  room={room}
                  hotel={room}
                />
              </Box>
            ))}
            {result.length === 0 && !loading && (
              <Text>There currently aren't any rooms</Text>
            )}
            {firstRender.current && <Loader />}
          </Center>
        </Container>
      </main>
    </>
  );
}
