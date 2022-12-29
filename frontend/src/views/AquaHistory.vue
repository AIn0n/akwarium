<script setup>
import Navbar from '../components/Navbar.vue';

import { useAlertsStore } from '../stores/alerts';
import { useAquariumStore } from '../stores/aquarium';
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const alertStore = useAlertsStore();
const aquariumStore = useAquariumStore();
const router = useRouter();


const logs = ref({});
const result = instance.get('/log-all', {aquarium: aquariumStore.aquarium_name})
  .then((res) => { logs.value = res.data })
  .catch((e) => {
    alertStore.set_danger('cannot get logs, try later');
    router.push('/aquaMonitor');
  })

console.log(logs);

</script>

<template lang="pug">
Navbar

</template>