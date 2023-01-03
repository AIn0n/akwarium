<script setup>
import { useRouter } from 'vue-router';
import instance from '../configs/axios_instance';
import { useAquariumStore } from '../stores/aquarium';

const router = useRouter();
const aquariumStore = useAquariumStore();

function logout() {
  let result = instance.post("/logout").then( res => { router.push("/") });
}
</script>

<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" @click="()=>{ router.push('/Aquariums') }">AquaFriends</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav" v-if="aquariumStore.isPicked">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="#" @click="()=>{ router.push('/aquaMonitor') }">aquaMonitor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="()=>{ router.push('/aquaLife') }">aquaLife</a>
        </li>
        <li class="nav-item me-auto">
          <a class="nav-link" @click="()=>{ router.push('/aquaHistory')}">aquaHistory</a>
        </li>
      </ul>
    </div>
  </div>
    <div class="collapse navbar-collapse me-auto" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" @click="()=>{ router.push('/settings') }">Settings</a>
        </li>
        <li class="nav-item me-auto">
          <a class="nav-link" @click="logout">Logout</a>
        </li>
      </ul>
    </div>
</nav>
</template>