import axios from "axios";
import { useDisclosure } from "@mantine/hooks";
import { Text, Group, Stack, Button, Flex, Container } from "@mantine/core";
import { message } from "antd";
import AddPaymentInfo from "~/components/AddPaymentInfo";
import useToken from "~/utils/useToken";
import { BookingInfo } from "~/types";

interface BookingProps {
  booking: BookingInfo;
}

export default function Booking(props: BookingProps) {
  const token = useToken();

  const [added, { open: add }] = useDisclosure();

  const handleCancel = async () => {
    try {
      await axios.delete(
        `http://127.0.0.1:5000/booking/booking/${props.booking.booking_ID}`
      );

      message.success("Booking successfully cancelled")
    } catch {
      message.error("Something went wrong while trying to cancel the booking")
    }
  };

  return (
    <Container>
      <Stack spacing="md">
        <Text>Booked: {props.booking.booking_date}</Text>
        <Flex justify="space-between">
          <Text>Hotel: {props.booking.hotel_ID}</Text>
          <Text>Room: {props.booking.room_number}</Text>
        </Flex>
        <Flex justify="space-between">
          <Text>Check in: {props.booking.scheduled_check_in_date}</Text>
          <Text>Check out: {props.booking.scheduled_check_out_date}</Text>
        </Flex>
        {token.role === "customer" && props.booking.canceled && (
          <Button onClick={handleCancel}>Cancel</Button>
        )}
        {token.role === "employee" && (
          <Flex justify="space-between">
            <AddPaymentInfo complete={added} setComplete={add} />
            <Button disabled={!added}>Convert To Renting</Button>
          </Flex>
        )}
      </Stack>
    </Container>
  );
}
