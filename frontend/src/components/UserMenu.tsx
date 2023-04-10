import Cookies from "js-cookie";
import jwt from "jwt-simple";
import { useRouter } from "next/router";
import Link from "next/link";
import { Text, Menu, UnstyledButton, Center } from "@mantine/core";
import { IconUserCircle, IconUser, IconBook, IconLogout } from "@tabler/icons";
import useToken from "~/utils/useToken";

export default function UserMenu() {
  const router = useRouter();
  const token = useToken();

  const handleLogout = () => {
    Cookies.remove("access_token");
    router.push("/login");
  };

  return (
    <Menu shadow="md">
      <Menu.Target>
        <UnstyledButton>
          <Center inline>
            <IconUserCircle />
            <Text size="sm" sx={{ paddingLeft: "8px" }}>
              {`${token.first_name} ${token.last_name}`}
            </Text>
          </Center>
        </UnstyledButton>
      </Menu.Target>

      {token.role === "customer" && (
        <Menu.Dropdown>
          <Link href="/user" style={{ textDecoration: "unset" }}>
            <Menu.Item icon={<IconUser size={14} />}>Account</Menu.Item>
          </Link>
          <Link href="/bookings" style={{ textDecoration: "unset" }}>
            <Menu.Item icon={<IconBook size={14} />}>Bookings</Menu.Item>
          </Link>
          <Link href="/rentings" style={{ textDecoration: "unset" }}>
            <Menu.Item icon={<IconBook size={14} />}>Rentings</Menu.Item>
          </Link>
          <Menu.Item icon={<IconLogout size={14} />} onClick={handleLogout}>
            Logout
          </Menu.Item>
        </Menu.Dropdown>
      )}
    </Menu>
  );
}
