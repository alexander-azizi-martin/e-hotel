import { create } from "zustand";

interface SearchQuery {
  startDate: string;
  endDate: string;
  maxPrice: null | number;
  hotelChain: null | string;
  category: null | number;
  numberOfRooms: null | number;
  roomCapacity: string;
  setDateRange: (dateRange: string[]) => void;
  setQuery: (query: SearchQueryOptional) => void;
}

interface SearchQueryOptional {
  startDate?: string;
  endDate?: string;
  maxPrice?: null | number;
  hotelChain?: null | string;
  category?: null | number;
  numberOfRooms?: null | number;
  roomCapacity?: string;
}

const useSearchQuery = create<SearchQuery>((set) => ({
  startDate: "",
  endDate: "",
  maxPrice: null,
  hotelChain: null,
  category: null,
  numberOfRooms: null,
  roomCapacity: "any",
  setDateRange: (dateRange: string[]) =>
    set((state) => ({
      ...state,
      startDate: dateRange[0],
      endDate: dateRange[1],
    })),
  setQuery: (query: SearchQueryOptional) =>
    set((state) => ({ ...state, ...query })),
}));

export default useSearchQuery;
