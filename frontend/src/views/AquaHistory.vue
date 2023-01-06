<script setup>
import Navbar from '../components/Navbar.vue';

import Plotly from 'plotly.js-dist-min';

import { useAlertsStore } from '../stores/alerts';
import { useAquariumStore } from '../stores/aquarium';
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onMounted, onBeforeMount } from 'vue';

const alertStore = useAlertsStore();
const aquariumStore = useAquariumStore();
const router = useRouter();
const chart = ref(null);

const logs = ref({});
let traces = {};
const params = ['GH', 'KH', 'NO2', 'NO3', 'PH'];
const layout = {
  title: 'water parameters over time',
  xaxis: {
    type: 'date',
    tickformat: '%Y-%m-%d',
    autorange: true
  },
  yaxis: {
    autorange: true,
    type: 'linear'
  }
}

// init each trace with proper obj
for (const param of params) {
  traces[param] = {
    x : [],
    y : [],
    mode: 'lines',
    name: param,
    type: 'scatter',
    line: {
      dash: 'solid',
      width: 4
    }
  }
}

onBeforeMount(()=>{
  instance.get('/log-all/' + aquariumStore.aquarium_name)
  .then((res) => { 
    logs.value = res.data.message;
    for (const log of logs.value.slice(1)) {
      for (const param of params) {
        traces[param].y.push(parseFloat(log[param]));
        traces[param].x.push(new Date(log.date));
      }
    }
  }).catch((e) => {
    alertStore.set_danger('cannot get logs, try later');
    router.push('/aquaMonitor');
  })
})

onMounted(()=>{
})

function generate_chart() {
  const data = Object.values(traces)
  console.log(data)
  Plotly.newPlot(chart.value, data, layout);
}
</script>

<template lang="pug">
Navbar
button(class="button" @click="generate_chart") click here to generate chart
div(ref='chart')
</template>