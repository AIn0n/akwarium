import { createRouter, createWebHistory } from 'vue-router';
import AquariumChooser from "../views/AquariumChooser.vue";
import LoginRegister from "../views/LoginRegister.vue";
import AquariumCreator from "../views/AquariumCreator.vue";
import Settings from "../views/Settings.vue";
import AquaMonitor from '../views/AquaMonitor.vue';
import AquaLife from '../views/AquaLife.vue';

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
  },
  {
    path: '/settings',
    name: 'settings',
    component: Settings
  },
  {
    path: '/aquaMonitor',
    name: 'aquaMonitor',
    component: AquaMonitor
  },
  {
    path: '/aquaLife',
    name: 'aquaLife',
    component: AquaLife
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router