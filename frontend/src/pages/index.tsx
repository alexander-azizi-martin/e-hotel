import axios from "axios";
import { GetServerSideProps } from "next";
import Header from "~/components/Header";

export default function Home() {
  

  return (
    <>
      <Header displayFilter />
      <main>
      </main>
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
