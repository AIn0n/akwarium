<script setup>
import { useRouter } from 'vue-router';
import instance from '../configs/axios_instance';

const router = useRouter();

function logout() {
  let result = instance.post("/logout").then( res => { router.push("/") });
}

function settings() {
  router.push("/settings")
}
</script>

<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="#">aquaMonitor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">aquaLife</a>
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