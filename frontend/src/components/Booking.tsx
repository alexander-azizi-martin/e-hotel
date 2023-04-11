import axios from "axios";
import dayjs from "dayjs";
import Cookies from "js-cookie";
import { useState } from "react";
import { useDisclosure } from "@mantine/hooks";
import { Text, Stack, Button, Flex, Paper } from "@mantine/core";
import { message } from "antd";
import AddPaymentInfo from "~/components/AddPaymentInfo";
import useToken from "~/utils/useToken";
import { BookingInfo, RoomInfo } from "~/types";

interface BookingProps {
  booking: BookingInfo;
}

export default function Booking({ booking }: BookingProps) {
  const token = useToken();

  const [added, { open: add }] = useDisclosure();
  const [display, setDisplay] = useState(true);

  const handleCancel = async () => {
    try {
      const access_token = Cookies.get("access_token");
      await axios.delete(
        `http://127.0.0.1:5000/booking/booking/${booking.booking_ID}`,
        { headers: { Authorization: `Bearer ${access_token}` } }
      );

      setDisplay(false);
      message.success("Booking successfully cancelled");
    } catch {
      message.error("Something went wrong while trying to cancel the booking");
    }
  };

  const handleConvertToRenting = async () => {
    try {
      const check_in = dayjs(booking.scheduled_check_in_date, "YYYY-MM-DD");
      const check_out = dayjs(booking.scheduled_check_out_date, "YYYY-MM-DD");
      const stay_duration = check_out.diff(check_in, "days");
      const { data: room } = await axios.get<RoomInfo>(
        `http://127.0.0.1:5000/room/room/${booking.hotel_ID}/${booking.room_number}`
      );

      await axios.post(
        `http://127.0.0.1:5000/rental/convert/${booking.booking_ID}`,
        {
          total_paid: stay_duration * room.price_per_night,
          discount: 0,
          additional_charges: 0,
        }
      );

      setDisplay(false);
      message.success("Booking successfully converted to a renting");
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  if (!display) return <></>;

  return (
    <Paper shadow="xs" p="lg" sx={{width: '300px'}}>
      <Stack spacing="md">
        <Text>
          <Text fw="bold">Booked:</Text> 
          {booking.booking_date}
        </Text>
        <Flex justify="space-between">
          <Text>
            <Text fw="bold">Hotel:</Text>
            {booking.hotel_ID}
          </Text>
          <Text align="right">
            <Text fw="bold">Room:</Text>
            {booking.room_number}
          </Text>
        </Flex>
        <Flex justify="space-between">
          <Text>
            <Text fw="bold">Check in:</Text>
            {booking.scheduled_check_in_date}
          </Text>
          <Text align="right">
            <Text fw="bold">Check out:</Text>
            {booking.scheduled_check_out_date}
          </Text>
        </Flex>
        {token.role === "customer" && !booking.canceled && (
          <Button onClick={handleCancel}>Cancel</Button>
        )}
        {token.role === "employee" && (
          <Flex justify="space-between">
            <AddPaymentInfo complete={added} setComplete={add} />
            <Button disabled={!added} onClick={handleConvertToRenting}>
              Convert To Renting
            </Button>
          </Flex>
        )}
      </Stack>
    </Paper>
  );
}
