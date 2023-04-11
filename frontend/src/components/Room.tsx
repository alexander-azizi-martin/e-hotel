import axios from "axios";
import { useState, useEffect } from "react";
import Cookies from "js-cookie";
import { useDisclosure } from "@mantine/hooks";
import {
  Paper,
  Text,
  Group,
  Rating,
  Modal,
  Center,
  Button,
} from "@mantine/core";
import { message } from "antd";
import RoomForm from "~/components/RoomForm";
import useToken from "~/utils/useToken";
import { RoomInfo, HotelInfo } from "~/types";

interface RoomProps {
  room: RoomInfo;
}

export default function Room(props: RoomProps) {
  const [opened, { open, close }] = useDisclosure();
  const [hotel, setHotel] = useState<HotelInfo | null>();
  const [room, setRoom] = useState(props.room);

  const token = useToken();

  useEffect(() => {
    axios
      .get<HotelInfo>(
        `http://127.0.0.1:5000/hotel/hotel/${props.room.hotel_id}`
      )
      .then((res) => {
        const { data } = res;
        setHotel(data);
      });
  }, [props.room.hotel_id]);

  const handleUpdate = async (values: RoomInfo) => {
    try {
      const access_token = Cookies.get("access_token");

      await axios.put(
        `http://127.0.0.1:5000/room/room`,
        {
          room_number: values.room_number,
          hotel_id: values.hotel_id,
          room_capacity: values.room_capacity,
          view_type: values.view_type,
          price_per_night: values.price_per_night,
          is_extendable: values.is_extendable,
          room_problems: values.room_problems,
        },
        { headers: { Authorization: `Bearer ${access_token}` } }
      );

      setRoom({ ...room, ...values });
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  return (
    <Paper shadow="xs" p="lg">
      <Text size="lg" weight={500}>
        Room {room.room_number}
      </Text>

      <Group position="apart" mt="sm">
        <Text>Hotel Chain </Text>

        <Rating value={hotel?.star_rating || 0} readOnly />
      </Group>
      <Text size="xs" color="dimmed"></Text>

      <Group position="apart" mt="sm">
        <Text>{room.room_capacity} Guests</Text>

        <Text>${room.price_per_night} per night</Text>
      </Group>

      <Center>
        {token.role === "customer" && (
          <Button size="md" compact>
            Book Now
          </Button>
        )}
        {token.role === "employee" && (
          <Button size="md" compact>
            Edit
          </Button>
        )}
      </Center>

      <Modal opened={opened} onClose={close} title="">
        <RoomForm
          room={props.room}
          onSubmit={handleUpdate}
        />
      </Modal>
    </Paper>
  );
}
