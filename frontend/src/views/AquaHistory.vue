<script setup>
import Navbar from '../components/Navbar.vue';

import Plotly from 'plotly.js-dist-min';

import { useAlertsStore } from '../stores/alerts';
import { useAquariumStore } from '../stores/aquarium';
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const alertStore = useAlertsStore();
const aquariumStore = useAquariumStore();
const router = useRouter();
const chart = ref(null);

const logs = ref({});
const result = instance.get('/log-all/' + aquariumStore.aquarium_name)
  .then((res) => { logs.value = res.data })
  .catch((e) => {
    alertStore.set_danger('cannot get logs, try later');
    router.push('/aquaMonitor');
  })

console.log(logs);

function foo()
{
  Plotly.newPlot(chart.value, [{ x: [1, 2, 3], y: [2, 1, 3], type: 'bar' }]);
}

</script>

<template lang="pug">
Navbar
div(ref='chart')
button(@click='foo') create chart
</template>