import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";
import { useDisclosure } from "@mantine/hooks";
import { Text, Stack, Button, Flex, Paper, Modal } from "@mantine/core";
import { message } from "antd";
import HotelForm from "~/components/HotelForm";
import useToken from "~/utils/useToken";
import { HotelInfo } from "~/types";

interface HotelProps {
  hotel: HotelInfo;
}

export default function Hotel(props: HotelProps) {
  const [opened, { close }] = useDisclosure();
  const [display, setDisplay] = useState(true);
  const [hotel, setHotel] = useState(props.hotel);

  const token = useToken();

  const handleUpdate = async (values: HotelInfo) => {
    try {
      const access_token = Cookies.get("access_token");

      await axios.put(`http://127.0.0.1:5000/hotel/hotel`, values, {
        headers: { Authorization: `Bearer ${access_token}` },
      });

      setHotel({ ...hotel, ...values });
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  const handleDelete = async () => {
    try {
      const access_token = Cookies.get("access_token");
      
      await axios.delete(
        `http://127.0.0.1:5000/hotel/hotel/${props.hotel.hotel_id}`,
        { headers: { Authorization: `Bearer ${access_token}` } }
      );

      setDisplay(false);
      message.success("Successfully deleted hotel");
    } catch {
      message.error("Something went wrong while trying to cancel the booking");
    }
  };

  if (!display) return <></>;

  return (
    <Paper shadow="xs" p="lg">
      <Stack spacing="md">
        <Flex justify="space-between">
          <Text>Hotel ID: {props.hotel.hotel_id}</Text>
          <Text>Chain ID: {props.hotel.chain_id}</Text>
        </Flex>
        <Text>Number of Rooms: {props.hotel.number_of_rooms}</Text>
        <Flex justify="space-between">
          <Text>Street Name: {props.hotel.address_street_name}</Text>
          <Text>Street Number: {props.hotel.address_street_number}</Text>
        </Flex>
        <Text>Address City: {props.hotel.address_city}</Text>
        <Flex justify="space-between">
          <Text>Region: {props.hotel.address_province_state}</Text>
          <Text>Country: {props.hotel.address_country}</Text>
        </Flex>

        {token.role === "employee" && (
          <Flex justify="space-between">
            <Button onClick={handleDelete}>Delete</Button>
            <Button>Edit</Button>
          </Flex>
        )}
      </Stack>

      <Modal opened={opened} onClose={close} title="Edit Hotel">
        <HotelForm hotel={hotel} onSubmit={handleUpdate} />
      </Modal>
    </Paper>
  );
}
