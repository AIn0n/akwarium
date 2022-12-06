<script setup>
import { useRouter } from 'vue-router';
import instance from '../configs/axios_instance';
import { useAquariumStore } from '../stores/aquarium';

const router = useRouter();
const aquariumStore = useAquariumStore();

function logout() {
  let result = instance.post("/logout").then( res => { router.push("/") });
}

console.log(aquariumStore.isPicked);
// why this function is even needed?
// well, this string "/settings" makes some problems in vue
// structure of bindings, so - don't try make it smaller again!
function settings() { router.push("/settings") }
function aquaLife() { router.push('/aquaLife') }
function aquaMonitor() { router.push('/aquaMonitor') }
function aquariumPicker() {
  aquariumStore.aquarium = "";
  router.push('/Aquariums')
}
</script>

<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#" @click="aquariumPicker">Navbar</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav" v-if="aquariumStore.isPicked">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="#" @click="aquaMonitor">aquaMonitor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="aquaLife">aquaLife</a>
        </li>
        <li class="nav-item me-auto">
          <a class="nav-link" href="#">aquaHistory</a>
        </li>
      </ul>
    </div>
  </div>
    <div class="collapse navbar-collapse me-auto" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" @click="settings">Settings</a>
        </li>
        <li class="nav-item me-auto">
          <a class="nav-link" @click="logout">Logout</a>
        </li>
      </ul>
    </div>
</nav>
</template>