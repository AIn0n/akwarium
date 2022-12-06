<script setup>
import Navbar from '../components/Navbar.vue';
import { onBeforeMount, ref } from 'vue';
import instance from '../configs/axios_instance';
import { useRouter } from "vue-router";
import { useAquariumStore } from '../stores/aquarium';

const router = useRouter();
const aquariums = ref();
const aquariumStore = useAquariumStore();

onBeforeMount(()=>{
  let result = instance.get('/aquarium')
    .then(res => { aquariums.value = res.data; });
});

function pickAquarium(aquarium_name) {
  aquariumStore.aquarium = aquarium_name;
  router.push('/aquaMonitor');
}

function gotoCreator(event) {
  router.push("/aquarium_creator");
}
</script>

<template>
<Navbar/>
<h3 class="display-6 my-3 text-center">hello again! Choose the aqaurium</h3>
<div v-for="aquarium in aquariums" class="card text-center w-50 mx-auto my-3">
  <img src="https://cdn.britannica.com/29/121829-050-911F77EC/freshwater-aquarium.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{{aquarium.name}}</h5>
    <p class="card-text"></p>
    <a href="#" class="btn btn-primary" @click="pickAquarium(aquarium.name)">Go somewhere</a>
  </div>
</div>
<div class="card text-center w-50 mx-auto my-3">
  <div class="card-body">
    <h5 class="card-title">Create new aquarium</h5>
    <p class="card-text"></p>
    <a class="btn btn-primary" @click="gotoCreator">+</a>
  </div>
</div>
</template>