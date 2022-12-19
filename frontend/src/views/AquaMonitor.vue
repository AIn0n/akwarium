<script setup>
import Navbar from '../components/Navbar.vue';
import { useAquariumStore } from '../stores/aquarium';
import { useAlertsStore } from '../stores/alerts';
import WaterTable from '../components/WaterTable.vue';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import instance from '../configs/axios_instance';

const aquariumStore = useAquariumStore();
const alertStore = useAlertsStore();
const router = useRouter();

onBeforeMount(()=>{
  const result = instance.get("aquarium/" + aquariumStore.aquarium)
    .then((res)=>{
      aquariumStore.aquarium = res.data;
    }).catch((e)=> {
      alertStore.set_danger("cannot connect to the server " + e);
      router.push('/Aquariums');
    });
});

const water = {
  KH: 10,
  GH: 10,
  NO3: 13,
  NO2: 12,
  PH: 6
};
const water_requirements = {
  water_min: {
    KH: 11,
    GH: 10,
    NO3: 10,
    NO2: 6,
    PH: 3,
  },
  water_max: {
    KH: 20,
    GH: 20,
    NO3: 15,
    NO2: 15,
    PH: 9
  }
}
</script>

<template>
  <Navbar />
  <div class="row">    
    <div class="list-group list-group-flush col-3">
      <a href="#" class="list-group-item list-group-item-action" v-for="fish in aquariumStore.aquarium.fish">
        {{fish.name}}
          <span class="position-absolute top-50 start-100 translate-middle badge rounded-pill bg-danger">
          {{fish.problems.length}}
          <span class="visually-hidden">problems</span>
        </span>
      </a>
    </div>
    <div class="col container text-center mx-3">
      <h3 class="display-6 my-3">{{ aquariumStore.aquarium.name }}</h3>
      <div class="row">
        <img src="https://cdn.britannica.com/29/121829-050-911F77EC/freshwater-aquarium.jpg" class="col-5 rounded mx-auto" alt="...">
        <table class="col table table-bordered table-striped table-hover mx-auto">
          <WaterTable :water="water" :requirements="water_requirements" />
        </table>
      </div>
      <div class="alert alert-warning my-3" role="alert">A simple info alert—check it out!</div>
      <div class="alert alert-danger my-3" role="alert">A simple info alert—check it out!</div>
      <div class="container text-center row">
        <button type="button" class="btn btn-outline-dark col mx-3">Save logs</button>
        <button type="button" class="btn btn-outline-dark col mx-3">Back to menu</button>
      </div>
    </div>
  </div>
</template>