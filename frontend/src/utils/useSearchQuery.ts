import { create } from "zustand";

interface SearchQuery {
  startDate: string;
  endDate: string;
  maxPrice: null | number;
  hotelChain: null | string;
  category: null | number;
  numberOfRooms: null | number;
  roomCapacity: string;
  startDateSet: (startDate: string) => void;
  endDateSet: (endDate: string) => void;
  maxPriceSet: (maxPrice: number) => void;
  hotelChainSet: (hotelChain: string) => void;
  categorySet: (category: number) => void;
  numberOfRoomsSet: (numberOfRooms: number) => void;
  roomCapacitySet: (roomCapacity: string) => void;
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
  startDateSet: (startDate: string) =>
    set((state) => ({ ...state, startDate })),
  endDateSet: (endDate: string) => set((state) => ({ ...state, endDate })),
  maxPriceSet: (maxPrice: number) => set((state) => ({ ...state, maxPrice })),
  hotelChainSet: (hotelChain: string) =>
    set((state) => ({ ...state, hotelChain })),
  categorySet: (category: number) => set((state) => ({ ...state, category })),
  numberOfRoomsSet: (numberOfRooms: number) =>
    set((state) => ({ ...state, numberOfRooms })),
  roomCapacitySet: (roomCapacity: string) =>
    set((state) => ({ ...state, roomCapacity })),
  setQuery: (query: SearchQueryOptional) =>
    set((state) => ({ ...state, ...query })),
}));

export default useSearchQuery;
