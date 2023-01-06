<script setup>
// components
import Navbar from '../components/Navbar.vue';
import WaterTable from '../components/WaterTable.vue';
import FishList from '../components/FishList.vue';
import AlertFromStore from '../components/AlertFromStore.vue';
// stores
import { useAquariumStore } from '../stores/aquarium';
import { useAlertsStore } from '../stores/alerts';
import { usePickedFishStore } from '../stores/pickedFish';
// vue elements and already configured elements
import { useRouter } from 'vue-router';
import { onBeforeMount } from 'vue';
import instance from '../configs/axios_instance';

const aquariumStore = useAquariumStore();
const pickedFishStore = usePickedFishStore();
const alertStore = useAlertsStore();
const router = useRouter();

onBeforeMount(()=>{
   instance.get("aquarium/" + aquariumStore.aquarium_name)
    .then((res)=>{
      aquariumStore.aquarium_object = res.data;
    }).catch((e)=> {
      alertStore.set_danger("cannot connect to the server " + e);
      router.push('/Aquariums');
    });
  instance.get('/log-newest/' + aquariumStore.aquarium_name)
    .then((res)=> {
      aquariumStore.water_object = Object.fromEntries(Object.entries(res.data.message).filter(([key]) => key != 'date'));
    }).catch((e)=> {
      alertStore.set_danger("cannot get last log " + e);
    });
  pickedFishStore.name = "";
});
</script>

<template>
  <Navbar />
  <div class="row">
    <FishList :fish_list="aquariumStore.aquarium_object.fish" />
    <div class="col container text-center mx-3">
      <h3 class="display-6 my-3">{{ aquariumStore.aquarium_name }}</h3>
      <div class="row my-3">
        <img :src="aquariumStore.aquarium_object['image']" class="col-5 rounded mx-auto" alt="...">
        <table class="col table table-bordered table-striped table-hover mx-auto">
          <WaterTable :water="aquariumStore.water_object" :water_min="aquariumStore.aquarium_object.water_min" :water_max="aquariumStore.aquarium_object.water_max" />
        </table>
      </div>
      <AlertFromStore />
      <div class="container text-center row">
        <button type="button" class="btn btn-outline-dark col mx-3">Save logs</button>
        <button type="button" class="btn btn-outline-dark col mx-3" @click="router.push('/WaterParamSetter')">Update Water parameters</button>
      </div>
    </div>
  </div>
</template>