import { useForm, isNotEmpty, hasLength } from "@mantine/form";
import Link from "next/link";
import {
  TextInput,
  PasswordInput,
  Button,
  Text,
  Stack,
  Container,
} from "@mantine/core";

interface CredentialFormProps {
  type: "login" | "signup";
  onSubmit?: (credentials: { username: string; password: string }) => void;
}

export default function CredentialForm(props: CredentialFormProps) {
  const form = useForm({
    initialValues: {
      username: "",
      password: "",
    },
    validate: {
      username: isNotEmpty("Enter your username"),
      password: hasLength({ min: 6 }, "Password must be at least 6 characters"),
    },
  });

  const handleSubmit = () => {
    if (props.onSubmit) form.onSubmit(props.onSubmit)();
  };

  return (
    <Container size="xs">
      <Stack spacing="md">
        <TextInput
          placeholder="Username"
          label="Username"
          {...form.getInputProps("username")}
        />
        <PasswordInput
          placeholder="Password"
          label="Password"
          {...form.getInputProps("password")}
        />
        {props.type == "login" ? (
          <Text>
            Don't have an account{" "}
            <Link href="/signup" style={{ textDecoration: "unset" }}>
              signup
            </Link>
            .
          </Text>
        ) : (
          <Text>
            Already have an account{" "}
            <Link href="/login" style={{ textDecoration: "unset" }}>
              login
            </Link>
            .
          </Text>
        )}
        <Button type="submit" onClick={handleSubmit}>
          {props.type.replace(/\b\w/g, (l) => l.toUpperCase())}
        </Button>
      </Stack>
    </Container>
  );
}
