<script setup>
import Navbar from '../components/Navbar.vue';
import { onBeforeMount, ref } from 'vue';
import instance from '../configs/axios_instance';
import { useRouter } from "vue-router";
import { useAquariumStore } from '../stores/aquarium';
import { useAlertsStore } from '../stores/alerts';
import AlertFromStore from '../components/AlertFromStore.vue';

const router = useRouter();
const aquariums = ref();
const aquariumStore = useAquariumStore();
const alertsStore = useAlertsStore();

onBeforeMount(()=>{
  aquariumStore.reset();
  let result = instance.get('/aquariums-names')
    .then(res => {
      aquariums.value = res.data; 
    }).catch((e)=> { alertsStore.set_danger("cannot connect to the server, try later")});
});

function pickAquarium(aquarium_name) {
  aquariumStore.aquarium_name = aquarium_name;
  router.push('/aquaMonitor');
}

function gotoCreator(event) {
  router.push("/aquarium_creator");
}
</script>

<template>
<Navbar/>
<h3 class="display-6 my-3 text-center">hello again! Choose the aqaurium</h3>
<AlertFromStore />
<div v-for="aquarium in aquariums" class="card text-center w-50 mx-auto my-3">
  <!-- next time add here aquarium['image'], not the direct link into the image -->
  <img :src="aquarium['image']" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{{aquarium['name']}}</h5>
    <a href="#" class="btn btn-primary" @click="pickAquarium(aquarium['name'])">check aquarium!</a>
  </div>
</div>
<div class="card text-center w-50 mx-auto my-3">
  <div class="card-body">
    <h5 class="card-title">Create new aquarium</h5>
    <a class="btn btn-primary" @click="gotoCreator">+</a>
  </div>
</div>
</template>