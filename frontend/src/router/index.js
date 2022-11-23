import { createRouter, createWebHistory } from 'vue-router';
import AquariumChooser from "../views/AquariumChooser.vue";
import LoginRegister from "../views/LoginRegister.vue";

const routes = [
  {
    path: "/",
    name: "LoginRegister",
    component: LoginRegister
  },
  {
    path: "/aquariums",
    name: "Aquariums",
    component: AquariumChooser
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router