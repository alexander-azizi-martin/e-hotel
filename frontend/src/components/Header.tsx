import Link from "next/link";
import { Flex, Text, Divider, Center } from "@mantine/core";
import { IconBed } from "@tabler/icons";
import FilterOptions from "./FilterOptions";
import SearchBar from "./SearchBar";
import DateRangePicker from "./DateRangePicker";
import UserMenu from "./UserMenu";

interface HeaderProps {
  displayFilter?: boolean;
}

export default function Header(props: HeaderProps) {
  return (
    <header>
      <Flex
        justify="space-between"
        align="center"
        wrap="wrap"
        sx={{
          minHeight: "65px",
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

        {props.displayFilter && (
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
            <DateRangePicker
              startDateLabel="Check In"
              endDateLabel="Check Out"
            />
          </Flex>
        )}

        <UserMenu />
      </Flex>

      <Divider />
    </header>
  );
}
