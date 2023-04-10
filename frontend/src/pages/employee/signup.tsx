import axios from "axios";
import Cookies from "js-cookie";
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
} from "@mantine/core";

export default function SignUp() {
  const router = useRouter();

  const form = useForm({
    initialValues: {
      ssn: "",
      firstName: "",
      lastName: "",
      password: "",
      city: "",
      streetName: "",
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
    const res = await axios.post("/customers", {
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
      const nextRes = await axios.post("/login", {
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
        <TextInput
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
        <Group align="center">
          <TextInput
            placeholder="Street Name"
            label="Street Name"
            {...form.getInputProps("streetName")}
          />
          <TextInput
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
