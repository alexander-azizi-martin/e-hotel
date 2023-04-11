import axios from "axios";
import { GetServerSideProps } from "next";
import Header from "~/components/Header";

export default function Home() {
  

  return (
    <>
      <Header />
      <main>
      </main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const access_token = context.req.cookies["access_token"];

  if (!access_token) {
    return {
      redirect: { destination: "/login", permanent: false },
    };
  }

  

  return {
    props: {},
  };
};
