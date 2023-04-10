import {
  Card,
  Text,
  Group,
  Rating,
  Container,
  Center,
  Button,
} from "@mantine/core";
import { RoomInfo } from "~/types";

interface RoomProps {
  room: RoomInfo;
}

export default function Room() {
  return (
    <Card shadow="sm" radius="md" withBorder>
      <Text size="lg" weight={500}>
        Room #123
      </Text>

      <Group position="apart" mt="sm">
        <Text>Hotel Chain</Text>

        <Rating value={3} readOnly />
      </Group>
      <Text size="xs" color="dimmed">
        Location
      </Text>

      <Group position="apart" mt="sm">
        <Text># Guests</Text>

        <Text>$100 per night</Text>
      </Group>

      <Center>
        <Button size="md" compact>
          Book Now
        </Button>
      </Center>
    </Card>
  );
}
