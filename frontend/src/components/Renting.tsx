import { Text, Stack, Flex, Paper } from "@mantine/core";
import { RentingInfo } from "~/types";

interface RentingProps {
  renting: RentingInfo;
}

export default function Renting({ renting }: RentingProps) {
  return (
    <Paper shadow="xs" p="lg">
      <Stack spacing="md">
        <Flex justify="space-between">
          <Text>Hotel id: {renting.hotel_ID}</Text>
          <Text>Room number: {renting.room_number}</Text>
        </Flex>
        <Flex justify="space-between">
          <Text>Total paid: {renting.total_paid}$</Text>
          <Text>Date paid: {renting.date_paid}</Text>
        </Flex>
        <Flex justify="space-between">
          <Text>Discount: {renting.discount}%</Text>
          <Text>Additional charges: {renting.date_paid}$</Text>
        </Flex>
        <Flex justify="space-between">
          <Text>Check in: {renting.check_in_date}</Text>
          <Text>Check out: {renting.check_out_date}</Text>
        </Flex>
      </Stack>
    </Paper>
  );
}
