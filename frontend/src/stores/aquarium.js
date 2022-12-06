import { defineStore } from "pinia";

export const useAquariumStore = defineStore({
  id: "aquarium",
  state: () => ({
    aquarium: ""
  })
});