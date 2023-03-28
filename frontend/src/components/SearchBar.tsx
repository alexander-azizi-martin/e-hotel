import { TextInput } from "@mantine/core";
import { IconSearch } from "@tabler/icons";

export default function SearchBar() {
  return (
    <TextInput
      placeholder="Destination"
      icon={<IconSearch />}
      radius="xl"
      sx={{
        boxShadow: "rgba(0, 0, 0, 0.08) 0px 1px 2px",
        borderRadius: "32px",
        width: "400px",
      }}
    />
  );
}
