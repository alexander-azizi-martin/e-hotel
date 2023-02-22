import { Text, Menu, UnstyledButton, Center } from "@mantine/core";
import { IconUserCircle, IconUser, IconBook, IconLogout } from "@tabler/icons";

interface UserMenuProps {
  username: string;
}

export default function UserMenu({ username }: UserMenuProps) {
  return (
    <Menu shadow="md">
      <Menu.Target>
        <UnstyledButton>
          <Center inline>
            <IconUserCircle />
            <Text size="sm" sx={{ paddingLeft: "8px" }}>
              {username}
            </Text>
          </Center>
        </UnstyledButton>
      </Menu.Target>

      <Menu.Dropdown>
        <Menu.Item icon={<IconUser size={14} />}>Account</Menu.Item>
        <Menu.Item icon={<IconBook size={14} />}>Bookings</Menu.Item>
        <Menu.Item icon={<IconLogout size={14} />}>Logout</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
