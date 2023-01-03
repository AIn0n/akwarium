import { defineStore } from "pinia";

export const useAlertsStore = defineStore({
  id: "alerts",
  state: () => ({
    picker_alert: "",
    picker_show: false,
    style: {
      "alert": true,
      "alert-danger": false,
      "alert-success": true,
      "text-center": true,
      "mx-5": true
    }
  }),
  actions: {
    set_success(msg) {
      this.picker_alert = msg;
      this.picker_show = true;
      this.style["alert-success"] = true;
      this.style["alert-danger"] = false;
    },
    set_danger(msg) {
      this.picker_alert = msg;
      this.picker_show = true;
      this.style["alert-success"] = false;
      this.style["alert-danger"] = true;
    },
    reset() {
      this.picker_alert = "";
      this.picker_show = false;
    }
  }
});