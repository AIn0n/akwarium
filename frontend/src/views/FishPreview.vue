<script setup>
// components
import Navbar from '../components/Navbar.vue';
import FishList from '../components/FishList.vue';
import WaterTable from '../components/WaterTable.vue';

// stores
import { useAquariumStore } from '../stores/aquarium';
import { usePickedFishStore } from '../stores/pickedFish';
import { useAlertsStore } from '../stores/alerts';

import { onBeforeMount, ref, watch } from 'vue';
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';

const aquariumStore = useAquariumStore();
const pickedFishStore = usePickedFishStore();
const alertsStore = useAlertsStore();

const router = useRouter();
const species = ref({});
const specie = ref({});
const fish = ref({});

watch(()=> pickedFishStore.name, (name)=>{ refresh_fish(name); });

function refresh_fish(name) {
  fish.value = aquariumStore.aquarium_object.fish.find(it => it.name === name);
  // I don't have any idea why find in example under not working
  for (const s of species.value) {
    if (fish.value.species === s.name)
      specie.value = s;
      return;
  }
}

onBeforeMount(()=>{
  const result = instance.get('/species')
    .then((res)=>{
      species.value = res.data;
      refresh_fish(pickedFishStore.name);
    }).catch((res)=>{
      alertsStore.set_danger("cannot connect to species database, try again later :(")
      router.push('/aquaMonitor');
    })
  
})

function eat_fish()
{
  const res = instance.delete('/delete-fish', {data: {
    'aquarium_name': aquariumStore.aquarium_name,
    'name': pickedFishStore.name
  }}).then((res)=>{
    alertsStore.set_success('successfully eaten the fish!');
    router.push('/aquaMonitor');
  }).catch((e)=> {
    alertsStore.set_danger('cannot eat fish, please try again later :(');
    router.push('/aquaMonitor');
  });
}

</script>

<template lang="pug">
Navbar
div(class="row")
  FishList(:fish_list="aquariumStore.aquarium_object.fish")
  div(class="col")
    h3 {{  pickedFishStore.name }}
    p fish's age: {{ fish.birth_date }}
    p specie: {{  fish.species }}
    h5 problems
    ul(class="list-group me-3")
      li(class="list-group-item list-group-item-danger" v-for="problem in fish.issues")
        div {{ problem.message }}
    div(class="row me-1")
      button(class="btn btn-danger text-center my-3 mx-3 col" @click="eat_fish") eat fish!
      button(class="btn btn-secondary text-center my-3 mx-3 col" @click="router.push('/aquaMonitor')") back to monitor
</template>