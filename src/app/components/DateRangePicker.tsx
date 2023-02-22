import { useLayoutEffect, useState } from "react";
import dayjs from "dayjs";

import { Flex, Popover, Text, UnstyledButton, Center } from "@mantine/core";
import { RangeCalendar } from "@mantine/dates";
import { Calendar } from "react-feather";

type DateRange = [Date | null, Date | null];

function formatDate(date: Date | null) {
  return !date ? "---, --/--/--" : dayjs(date).format("ddd, MM/DD/YY");
}

export default function DateRangePicker() {
  const [dateRange, setDateRange] = useState<DateRange>([null, null]);

  useLayoutEffect(() => {
    if (dateRange[0] && (!dateRange[1] || dateRange[0] > dateRange[1])) {
      const newValue = [new Date(dateRange[0]), new Date(dateRange[0])];
      newValue[1].setDate(newValue[0].getDate() + 1);

      setDateRange(newValue as DateRange);
    }
  }, [dateRange]);

  return (
    <Flex sx={{ width: "300px" }}>
      <Popover position="bottom" withArrow shadow="md">
        <Popover.Target>
          <UnstyledButton>
            <Center inline>
              <Text
                size={!dateRange[0] ? "md" : "sm"}
                sx={{ paddingRight: "8px" }}
              >
                {formatDate(dateRange[0])}
              </Text>
              <Calendar />
            </Center>
          </UnstyledButton>
        </Popover.Target>

        <Popover.Dropdown>
          <RangeCalendar
            value={dateRange}
            onChange={setDateRange}
            weekendDays={[]}
            minDate={new Date()}
          />
        </Popover.Dropdown>
      </Popover>

      <Text size="md" sx={{ padding: "0px 10px" }}>
        to
      </Text>

      <Popover position="bottom" withArrow shadow="md">
        <Popover.Target>
          <UnstyledButton>
            <Center inline>
              <Text
                size={!dateRange[1] ? "md" : "sm"}
                sx={{ paddingRight: "8px" }}
              >
                {formatDate(dateRange[1])}
              </Text>
              <Calendar />
            </Center>
          </UnstyledButton>
        </Popover.Target>

        <Popover.Dropdown>
          <RangeCalendar
            value={dateRange}
            onChange={setDateRange}
            weekendDays={[]}
            minDate={new Date()}
          />
        </Popover.Dropdown>
      </Popover>
    </Flex>
  );
}
