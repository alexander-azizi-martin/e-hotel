import { ChangeEvent } from "react";
import { useToggle } from "@mantine/hooks";
import { useForm } from "@mantine/form";
import {
  Box,
  Flex,
  Center,
  Modal,
  Button,
  Title,
  Text,
  Divider,
  RangeSlider,
  TextInput,
  Rating,
  SegmentedControl,
  Radio,
  NumberInput,
} from "@mantine/core";
import { IconAdjustments } from "@tabler/icons";

export default function FilterOptions() {
  const [open, toggle] = useToggle();
  const form = useForm({
    initialValues: {
      minPrice: 0,
      maxPrice: 100,
      hotelChain: "",
      category: 0,
      numberOfRooms: null,
      roomCapacity: "any",
    },
  });

  return (
    <>
      <Button
        onClick={() => toggle()}
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
      <Modal
        opened={open}
        onClose={() => toggle()}
        size="800px"
        transition="scale"
        overflow="inside"
        centered
        title={
          <Center>
            <Title order={4}>Filters</Title>
          </Center>
        }
      >
        <Box sx={{ padding: "0px 20px" }}>
          <Flex rowGap="20px" direction="column" sx={{ margin: "20px" }}>
            <Title order={3} sx={{ marginBottom: "-20px" }}>
              Price
            </Title>
            <Flex align="flex-end" justify="center">
              <TextInput
                label="Min price"
                icon="$"
                {...form.getInputProps("minPrice")}
                onChange={(event) => {
                  if (/^\d+$/.test(event.target.value)) {
                    form.setValues({ minPrice: parseInt(event.target.value) });
                  }
                }}
              />
              <Text sx={{ padding: "10px" }}>-</Text>
              <TextInput
                label="Max price"
                icon="$"
                {...form.getInputProps("maxPrice")}
                onChange={(event) => {
                  if (/^\d+$/.test(event.target.value)) {
                    form.setValues({ maxPrice: parseInt(event.target.value) });
                  }
                }}
              />
            </Flex>

            <Box sx={{ width: "80%", margin: "auto" }}>
              <RangeSlider
                step={1}
                minRange={0}
                value={[form.values.minPrice, form.values.maxPrice]}
                onChange={(newRange) => {
                  form.setValues({
                    minPrice: newRange[0],
                    maxPrice: newRange[1],
                  });
                }}
              />
            </Box>
          </Flex>

          <Divider />

          <Flex rowGap="20px" direction="column" sx={{ margin: "20px" }}>
            <Title order={3}>Hotel</Title>

            <Flex direction="column" rowGap="8px">
              <Text>Hotel Chain</Text>
              <Radio.Group {...form.getInputProps("hotelChain")}>
                <Radio
                  value="Chain1"
                  label="Chain1"
                  onClick={() => {
                    if (form.values.hotelChain === "Chain1") {
                      form.setValues({ hotelChain: "" });
                    }
                  }}
                />
                <Radio
                  value="Chain2"
                  label="Chain2"
                  onClick={() => {
                    if (form.values.hotelChain === "Chain2") {
                      form.setValues({ hotelChain: "" });
                    }
                  }}
                />
                <Radio
                  value="Chain3"
                  label="Chain3"
                  onClick={() => {
                    if (form.values.hotelChain === "Chain3") {
                      form.setValues({ hotelChain: "" });
                    }
                  }}
                />
                <Radio
                  value="Chain4"
                  label="Chain4"
                  onClick={() => {
                    if (form.values.hotelChain === "Chain4") {
                      form.setValues({ hotelChain: "" });
                    }
                  }}
                />
              </Radio.Group>
            </Flex>

            <Flex direction="column" rowGap="8px">
              <Text>Category</Text>
              <Rating size="lg" {...form.getInputProps("category")} />
            </Flex>

            <Flex direction="column" rowGap="8px">
              <Text>Number of Rooms</Text>
              <NumberInput
                sx={{ width: "50%" }}
                {...form.getInputProps("numberOfRooms")}
              />
            </Flex>
          </Flex>

          <Divider />

          <Flex rowGap="20px" direction="column" sx={{ margin: "20px" }}>
            <Title order={3}>Room Capacity</Title>

            <SegmentedControl
              data={[
                { label: "Any", value: "any" },
                { label: "1", value: "1" },
                { label: "2", value: "2" },
                { label: "3", value: "3" },
                { label: "4", value: "4" },
                { label: "5", value: "5" },
                { label: "6", value: "6" },
                { label: "7", value: "7" },
                { label: "8+", value: "8" },
              ]}
              {...form.getInputProps("roomCapacity")}
            />
          </Flex>
        </Box>
      </Modal>
    </>
  );
}
