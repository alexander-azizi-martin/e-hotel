import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";
import { Container } from "@mantine/core";
import { message } from "antd";
import Header from "~/components/Header";
import RoomForm from "~/components/RoomForm";
import { RoomInfo } from "~/types";

export default function AddRoom() {
  const [formReset, setFormReset] = useState(() => () => {});

  const handleSubmit = async (values: RoomInfo) => {
    try {
      const access_token = Cookies.get("access_token");

      await axios.post("http://127.0.0.1:5000/room/room", values, {
        headers: { Authorization: `Bearer ${access_token}` },
      });

      formReset();
      message.success("Room successfully created");
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  return (
    <>
      <Header />
      <main>
        <Container sx={{ marginTop: "20px" }}>
          <RoomForm onSubmit={handleSubmit} setFormReset={setFormReset} />
        </Container>
      </main>
    </>
  );
}
