import Link from "next/link";
import { Flex, Text, Divider, Center } from "@mantine/core";
import { IconBed } from "@tabler/icons";
import FilterOptions from "./FilterOptions";
import SearchBar from "./SearchBar";
import DateRangePicker from "./DateRangePicker";
import UserMenu from "./UserMenu";

export default function Header() {
  return (
    <header>
      <Flex
        justify="space-between"
        align="center"
        wrap="wrap"
        sx={{
          height: "max-content",
          padding: "10px",
        }}
      >
        <Link href="/" style={{ textDecoration: "unset" }}>
          <Center inline sx={{ color: "black" }}>
            <IconBed size="32px" />
            <Text size="xl" sx={{ paddingLeft: "8px" }}>
              E-hotels
            </Text>
          </Center>
        </Link>

        <Flex
          align="center"
          justify="center"
          rowGap="20px"
          columnGap="30px"
          wrap="wrap"
          sx={{ "@media (max-width: 1115px)": { order: 3 } }}
        >
          <FilterOptions />
          <SearchBar />
          <DateRangePicker />
        </Flex>

        <UserMenu username="username" />
      </Flex>

      <Divider />
    </header>
  );
}
