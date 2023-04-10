import axios from "axios";
import jwt from "jwt-simple";
import Cookies from "js-cookie";
import { GetServerSideProps } from "next";
import { useRouter } from "next/router";
import { useForm, isNotEmpty, hasLength } from "@mantine/form";
import Link from "next/link";
import {
  TextInput,
  PasswordInput,
  Button,
  Text,
  Stack,
  Center,
  Group,
  NumberInput,
} from "@mantine/core";
import { Token } from "~/types";

export default function SignUp() {
  const router = useRouter();

  const form = useForm({
    initialValues: {
      ssn: null,
      firstName: "",
      lastName: "",
      password: "",
      city: "",
      streetName: null,
      streetNumber: "",
      country: "",
      region: "",
    },
    validate: {
      ssn: isNotEmpty("Enter your ssn"),
      firstName: isNotEmpty("Enter your first name"),
      lastName: isNotEmpty("Enter your last name"),
      streetName: isNotEmpty("Enter your street name"),
      streetNumber: isNotEmpty("Enter your street number"),
      city: isNotEmpty("Enter your city"),
      country: isNotEmpty("Enter your country"),
      region: isNotEmpty("Enter your region"),
      password: hasLength({ min: 6 }, "Password must be at least 6 characters"),
    },
  });

  const handleSubmit = form.onSubmit(async (info) => {
    const res = await axios.post("http://127.0.0.1:5000/auth/customers", {
      customer_SSN_SIN: info.ssn,
      first_name: info.firstName,
      last_name: info.lastName,
      address_street_name: info.streetName,
      address_street_number: info.streetNumber,
      address_city: info.city,
      address_province_state: info.region,
      address_country: info.country,
      password: info.password,
    });

    if (res.status == 200) {
      const nextRes = await axios.post("http://127.0.0.1:5000/auth/login", {
        user_SSN_SIN: info.ssn,
        password: info.password,
        role: "customer",
      });

      Cookies.set("access_token", nextRes.data["access_token"]);
      router.push("/");
    } else {
      form.setErrors({ ssn: res.data.message });
    }
  });

  return (
    <Center sx={{ height: "100%" }}>
      <Stack spacing="md">
        <NumberInput
          placeholder="SSN"
          label="SSN"
          {...form.getInputProps("ssn")}
        />
        <Group align="center">
          <TextInput
            placeholder="First Name"
            label="First Name"
            {...form.getInputProps("firstName")}
          />
          <TextInput
            placeholder="Last Name"
            label="Last Name"
            {...form.getInputProps("lastName")}
          />
        </Group>
        <Group>
          <TextInput
            placeholder="Street Name"
            label="Street Name"
            {...form.getInputProps("streetName")}
          />
          <NumberInput
            placeholder="Street Number"
            label="Street Number"
            {...form.getInputProps("streetNumber")}
          />
        </Group>
        <TextInput
          placeholder="City"
          label="City"
          {...form.getInputProps("city")}
        />
        <Group align="center">
          <TextInput
            placeholder="Country"
            label="Country"
            {...form.getInputProps("country")}
          />
          <TextInput
            placeholder="Region"
            label="Region"
            {...form.getInputProps("region")}
          />
        </Group>
        <PasswordInput
          placeholder="Password"
          label="Password"
          {...form.getInputProps("password")}
        />

        <Text>
          Already have an account{" "}
          <Link href="/login" style={{ textDecoration: "unset" }}>
            login
          </Link>
          .
        </Text>

        <Button type="submit" onClick={handleSubmit as any}>
          Sign Up
        </Button>
      </Stack>
    </Center>
  );
}

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const access_token = context.req.cookies["session_token"];

  if (access_token) {
    const token: Token = jwt.decode(access_token, "", false);

    return {
      redirect: {
        destination: token.role === "customer" ? "/" : "/employee",
        permanent: false,
      },
    };
  }

  return {
    props: {},
  };
};
