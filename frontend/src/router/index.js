import { createRouter, createWebHistory } from 'vue-router';
import AquariumChooser from "../views/AquariumChooser.vue";
import LoginRegister from "../views/LoginRegister.vue";
import AquariumCreator from "../views/AquariumCreator.vue";

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
  },
  {
    path: "/aquarium_creator",
    name: "creator",
    component: AquariumCreator
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router