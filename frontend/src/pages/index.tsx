import axios from "axios";
import dayjs from "dayjs";
import { useEffect, useRef, useState } from "react";
import { Container, Text, Box, Center, Loader, Flex } from "@mantine/core";
import Room from "~/components/Room";
import Header from "~/components/Header";
import useSearchQuery from "~/utils/useSearchQuery";
import { HotelChainSearch, HotelChainInfo, RoomInfo, HotelInfo } from "~/types";

type RoomQuery = { room: RoomInfo; hotel: HotelInfo };

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
  const [hotelChains, setHotelChains] = useState<HotelChainInfo[]>([]);

  useEffect(() => {
    axios
      .get<HotelChainInfo[]>("http://127.0.0.1:5000/hotel_chain/hotel_chain")
      .then((res) => {
        const { data } = res;

        setHotelChains(data);
      });
  }, []);

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

  const rooms: RoomQuery[] = [];
  for (let hotelChain of result) {
    for (let hotel of hotelChain.hotels) {
      for (let room of hotel.rooms) {
        rooms.push({ room, hotel });
      }
    }
  }

  return (
    <>
      <Header displayFilter />
      <main>
        <Container sx={{ marginTop: "20px", marginBottom: "20px" }}>
          <Center>
            <Flex wrap="wrap" gap="30px">
              {rooms.map((result) => (
                <Room
                  key={`${result.room.room_number}-${result.room.hotel_id}`}
                  room={result.room}
                  hotel={result.hotel}
                  hotelChains={hotelChains}
                />
              ))}
              {result.length === 0 && !loading && (
                <Text>No rooms available with the given criteria</Text>
              )}
              {firstRender.current && <Loader />}
            </Flex>
          </Center>
        </Container>
      </main>
    </>
  );
}
