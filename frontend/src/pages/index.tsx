import axios from "axios";
import { useEffect, useRef } from "react";
import { GetServerSideProps } from "next";
import Header from "~/components/Header";
import useSearchQuery from "~/utils/useSearchQuery";

export default function Home() {
  const {
    startDate,
    endDate,
    maxPrice,
    hotelChain,
    category,
    numberOfRooms,
    roomCapacity,
  } = useSearchQuery((state) => state);
  const debounceState = useRef<null | number>(null);

  useEffect(() => {
    
  }, [
    startDate,
    endDate,
    maxPrice,
    hotelChain,
    category,
    numberOfRooms,
    roomCapacity,
  ]);

  return (
    <>
      <Header displayFilter />
      <main></main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const isLoggedIn = context.req.cookies["access_token"];

  if (!isLoggedIn) {
    return {
      redirect: { destination: "/login", permanent: false },
    };
  }

  return {
    props: {},
  };
};
