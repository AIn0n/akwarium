import { defineStore } from "pinia";

export const useAlertsStore = defineStore({
  id: "alerts",
  state: () => ({
    picker_alert: "",
    picker_show: false
  })
});