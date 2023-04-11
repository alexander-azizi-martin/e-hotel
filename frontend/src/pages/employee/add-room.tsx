import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";
import { Container } from "@mantine/core";
import { message } from "antd";
import RoomForm from "~/components/RoomForm";
import { RoomInfo } from "~/types";

export default function AddRoom() {
  const [formReset, setFormReset] = useState(() => () => {});

  const handleSubmit = async (values: RoomInfo) => {
    try {
      const access_token = Cookies.get("access_token");

      await axios.post("/room/room", values, {
        headers: { Authorization: `Bearer ${access_token}` },
      });

      formReset();
      message.success("Room successfully created");
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  return (
    <Container>
      <RoomForm onSubmit={handleSubmit} setFormReset={setFormReset} />
    </Container>
  );
}
