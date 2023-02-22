import { Button } from "@mantine/core";
import { IconAdjustments } from "@tabler/icons";

export default function FilterOptions() {
  return (
    <Button
      leftIcon={<IconAdjustments />}
      variant="outline"
      color="dark"
      sx={{
        borderColor: "rgb(206, 212, 218)",
        ":hover": { backgroundColor: "unset" },
      }}
    >
      Filter
    </Button>
  );
}
