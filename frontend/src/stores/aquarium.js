import { defineStore } from "pinia";

export const useAquariumStore = defineStore({
  id: "aquarium",
  state: () => ({
    aquarium: ""
  }),
  getters: {
    isPicked: (state) => {
      return state.aquarium.length > 0;
    }
  }
});