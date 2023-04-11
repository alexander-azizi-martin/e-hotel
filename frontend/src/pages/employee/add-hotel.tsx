import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";
import { Container } from "@mantine/core";
import { message } from "antd";
import HotelForm from "~/components/HotelForm";
import { HotelInfo } from "~/types";

export default function AddHotel() {
  const [formReset, setFormReset] = useState(() => () => {});

  const handleSubmit = async (values: HotelInfo) => {
    try {
      const access_token = Cookies.get("access_token");

      await axios.post("/hotel/hotel", values, {
        headers: { Authorization: `Bearer ${access_token}` },
      });

      formReset();
      message.success("Hotel successfully created");
    } catch (error: any) {
      message.error(error.response.data.message);
    }
  };

  return (
    <Container>
      <HotelForm onSubmit={handleSubmit} setFormReset={setFormReset} />
    </Container>
  );
}