import axios from "axios";
import dayjs from "dayjs";
import { GetServerSideProps } from "next";
import { Center, Container, Table } from "@mantine/core";
import Header from "~/components/Header";

interface CapacityInfo {
  hotel_chain_name: string;
  chain_id: number;
  hotel_id: number;
  room_number: number;
  room_capacity: number;
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
                  <th>Room Number</th>
                  <th>Capacity</th>
                </tr>
              </thead>
              <tbody>
                {props.capacitiesInfo.map((capacityInfo) => (
                  <tr
                    key={`${capacityInfo.hotel_chain_name}-${capacityInfo.room_number}`}
                  >
                    <td>{capacityInfo.hotel_chain_name}</td>
                    <td>{capacityInfo.room_number}</td>
                    <td>{capacityInfo.room_capacity}</td>
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

  const { data } = await axios.get<CapacityInfo[]>(
    "http://127.0.0.1:5000/hotel/hotel/total_capacity"
  );

  return {
    props: { capacitiesInfo: data },
  };
};
