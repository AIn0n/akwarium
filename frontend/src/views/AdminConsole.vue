<script setup>
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import { useAlertsStore } from '../stores/alerts';

const router = useRouter();
const species = ref({});
const alertsStore = useAlertsStore();

onBeforeMount(()=>{
  const result = instance.get('/species-names')
    .then((res)=>{
      species.value = res.data;
    }).catch((e)=>{
      alertsStore.set_danger("cannot get list of species from server, try later");
      router.push('/Aquariums');
    });
})

</script>

<template lang="pug">
div(class="container row")
  div(class="col-3 list-group")
    div(class="list-group-item" v-for="specie in species")
      a {{ specie }}
      button(type="button" class="btn-close position-absolute start-100" aria-label="Close")
</template>