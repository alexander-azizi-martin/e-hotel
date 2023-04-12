import axios from "axios";
import dayjs from "dayjs";
import { GetServerSideProps } from "next";
import { Center, Container, Table } from "@mantine/core";
import Header from "~/components/Header";
import { HotelInfo } from "~/types";

interface CapacityInfo {
  total_capacity: number;
  hotel_id: number;
}

interface HotelsProps {
  capacitiesInfo: CapacityInfo[];
}

export default function Hotels(props: HotelsProps) {
  return (
    <>
      <Header />
      <main>
        <Container size="sm">
          <Center sx={{ marginTop: "20px", marginBottom: "20px" }}>
            <Table>
              <thead>
                <tr>
                  <th>Hotel</th>
                  <th>Capacity</th>
                </tr>
              </thead>
              <tbody>
                {props.capacitiesInfo.map((capacityInfo) => (
                  <tr key={capacityInfo.hotel_id}>
                    <td>{capacityInfo.hotel_id}</td>
                    <td>{capacityInfo.total_capacity}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Center>
        </Container>
      </main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<HotelsProps> = async (
  context
) => {
  const access_token = context.req.cookies["access_token"];

  if (!access_token) {
    return {
      redirect: { destination: "/login", permanent: false },
    };
  }

  const { data: hotels } = await axios.get<HotelInfo[]>(
    `http://127.0.0.1:5000/hotel/hotel`
  );

  const capacityInfo: CapacityInfo[] = [];
  for (let hotel of hotels) {
    const {
      data: { total_capacity },
    } = await axios.get<{ total_capacity: number }>(
      `http://127.0.0.1:5000/hotel/hotel/total_capacity/${hotel.hotel_id}`
    );
    capacityInfo.push({ hotel_id: hotel.hotel_id, total_capacity });
  }

  return {
    props: { capacitiesInfo: capacityInfo },
  };
};
