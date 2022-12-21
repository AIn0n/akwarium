import { defineStore } from "pinia";

export const usePickedFishStore = defineStore({
  id: "pickedFish",
  state: ()=> {
    name: ""
  },
  actions: {
    reset() {
      this.name = "";
    }
  }
});