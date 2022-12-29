<script setup>
import { useAquariumStore } from '../stores/aquarium';
import { useAlertsStore } from '../stores/alerts';

import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const aquariumStore = useAquariumStore();
const alertStore = useAlertsStore();

const router = useRouter();

const water = ref({
  kh: 0,
  gh: 0,
  ph: 0,
  no2: 0,
  no3: 0
});

function add_new_stats(water)
{
  let input = { ...water, aquarium: aquariumStore.aquarium_name };
  instance.post('/log-add', input)
    .then((res)=>{
      alertStore.set_success("successfully changed water parameters");
    }).catch((e)=>{
      alertStore.set_danger("cannot add water parameters, please try later");
    })
  router.push('/aquaMonitor');
  console.log(input);
}

</script>


<template lang="pug">
h4(class="display-6 text-center my-3") Add water parameters by hand
div(class="row my-3 mx-3")
  div(class="col" v-for="key in Object.keys(water)")
    label(class="form-label") {{  key }}
    input(type="number" class="form-control" v-model="water[key]")
div(class="container my-3 text-center w-75")
  div(class="row")
    button(class="btn btn-primary col mx-3" @click="add_new_stats(water)") add new stats
    button(class="btn btn-secondary col mx-3" @click="router.push('/aquaMonitor')") back to aquaMonitor
</template>