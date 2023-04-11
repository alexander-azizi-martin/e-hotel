import axios from "axios";
import { GetServerSideProps } from "next";
import { Stack, Text, Center } from "@mantine/core";
import Header from "~/components/Header";
import Hotel from "~/components/Hotel";
import { HotelInfo } from "~/types";

interface HotelsProps {
  hotels: HotelInfo[];
}

export default function Hotels(props: HotelsProps) {
  return (
    <>
      <Header />
      <main>
        <Center sx={{ marginTop: "20px" }}>
          <Stack spacing="md">
            {props.hotels.map((hotel) => (
              <Hotel hotel={hotel} key={hotel.hotel_id} />
            ))}
            {props.hotels.length === 0 && (
              <Text>There currently aren't any hotels</Text>
            )}
          </Stack>
        </Center>
      </main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<HotelsProps> = async (
  context
) => {
  const access_token = context.req.cookies["access_token"];

  if (!access_token) {
    return {
      redirect: { destination: "/login", permanent: false },
    };
  }

  const { data } = await axios.get<HotelInfo[]>(
    `http://127.0.0.1:5000/hotel/hotel/search`,
    {
      headers: { Authorization: `Bearer ${access_token}` },
    }
  );

  return {
    props: { hotels: data },
  };
};
