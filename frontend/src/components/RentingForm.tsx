import { useEffect } from "react";
import { useForm, isNotEmpty, isEmail, isInRange } from "@mantine/form";
import {
  Button,
  Stack,
  Group,
  NumberInput,
  Text,
} from "@mantine/core";
import DateRangePicker from "~/components/DateRangePicker";
import { RentingFormInfo } from "~/types";

interface HotelForm {
  setFormReset?: (formReset: () => void) => void;
  onSubmit: (hotel: RentingFormInfo) => void;
}

export default function RentingForm(props: HotelForm) {
  const form = useForm({
    initialValues: {
      discount: 0,
      additional_charges: 0,
      hotel_ID: null,
      room_number: null,
      customer_SSN_SIN: null,
      check_in_date: "",
      check_out_date: "",
    },
    validate: {
      discount: isInRange(
        { min: 0, max: 100 },
        "Discount must be between 0 to 100"
      ),
      additional_charges: isInRange(
        { min: 0 },
        "Additional charges must be positive"
      ),
      hotel_ID: isNotEmpty("Provide a hotel id"),
      room_number: isNotEmpty("Provide a room number"),
      customer_SSN_SIN: isNotEmpty("Provide customer SSN"),
      check_in_date: isNotEmpty("Select check in and check out dates"),
      check_out_date: isNotEmpty("Select check in and check out dates"),
    },
  });

  const handleDateChange = (dateRange: string[]) => {
    form.setValues({
      check_in_date: dateRange[0],
      check_out_date: dateRange[1],
    });
  };

  useEffect(() => {
    if (props.setFormReset) props.setFormReset(form.reset);
  }, [form.reset, props.setFormReset]);

  return (
    <Stack spacing="md">
      <NumberInput
        placeholder="Customer SSN"
        label="Customer SSN"
        {...form.getInputProps("customer_SSN_SIN")}
      />
      <Stack>
        <DateRangePicker setDateRange={handleDateChange} />
        <Text color="red" size="xs">
          {form.errors.check_in_date}
        </Text>
      </Stack>
      <Group align="center">
        <NumberInput
          placeholder="Hotel Id"
          label="Hotel Id"
          {...form.getInputProps("hotel_ID")}
        />
        <NumberInput
          placeholder="Room number"
          label="Room number"
          {...form.getInputProps("room_number")}
        />
      </Group>
      <Group align="center">
        <NumberInput
          placeholder="Discount"
          icon="%"
          label="Discount"
          {...form.getInputProps("discount")}
        />
        <NumberInput
          placeholder="Additional Charges"
          icon="$"
          label="Additional Charges"
          {...form.getInputProps("additional_charges")}
        />
      </Group>
      <Button
        type="submit"
        onClick={form.onSubmit(props.onSubmit as any) as any}
      >
        Submit
      </Button>
    </Stack>
  );
}
