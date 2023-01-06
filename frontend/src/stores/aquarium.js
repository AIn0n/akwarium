import { defineStore } from "pinia";

export const useAquariumStore = defineStore({
  id: "aquarium",
  state: () => ({
    aquarium_name: "",
    aquarium_object: {},
    water_object : {},
  }),
  getters: {
    isPicked: (state) => {
      return state.aquarium_name != "";
    }
  },
  actions: {
    reset() {
      this.aquarium_name = "";
      this.aquarium_object = {};
      this.water_object = {};
    }
  }
});