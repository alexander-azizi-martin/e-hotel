import jwt from "jwt-simple";
import axios from "axios";
import { GetServerSideProps } from "next";
import { Stack, Text, Center } from "@mantine/core";
import Header from "~/components/Header";
import Booking from "~/components/Booking";
import { BookingInfo, Token } from "~/types";

interface BookingsProps {
  bookings: BookingInfo[];
}

export default function Bookings(props: BookingsProps) {
  return (
    <>
      <Header />
      <main>
        <Center sx={{ marginTop: "20px" }}>
          <Stack spacing="md">
            {props.bookings.map((booking) => (
              <Booking booking={booking} key={booking.booking_ID} />
            ))}
            {props.bookings.length === 0 && (
              <Text>You do not currently have any bookings</Text>
            )}
          </Stack>
        </Center>
      </main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<BookingsProps> = async (
  context
) => {
  const access_token = context.req.cookies["access_token"];

  if (!access_token) {
    return {
      redirect: { destination: "/login", permanent: false },
    };
  }

  const token: Token = jwt.decode(access_token, "", true);

  if (token.role === "employee") {
    return {
      redirect: { destination: "/employee/booking", permanent: false },
    };
  }

  const { data } = await axios.get<BookingInfo[]>(
    "http://127.0.0.1:5000/booking/booking",
    {
      headers: { Authorization: `Bearer ${access_token}` },
    }
  );

  return {
    props: { bookings: data },
  };
};
