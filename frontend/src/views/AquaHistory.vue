<script setup>
import Navbar from '../components/Navbar.vue';

import Plotly from 'plotly.js-dist-min';

import { useAlertsStore } from '../stores/alerts';
import { useAquariumStore } from '../stores/aquarium';
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';

const alertStore = useAlertsStore();
const aquariumStore = useAquariumStore();
const router = useRouter();
const chart = ref(null);
const show_logs = ref(true);

const logs = ref({});
let traces = {};
const params = ['GH', 'KH', 'NO2', 'NO3', 'PH'];

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
    if (logs.value.length > 2) {
      for (const log of logs.value.slice(1)) {
        for (const param of params) {
          traces[param].y.push(parseFloat(log[param]));
          traces[param].x.push(new Date(log.date));
        }
      }
    } else {
      show_logs.value = false;
    }
  }).catch((e) => {
    alertStore.set_danger('cannot get logs, try later');
    router.push('/aquaMonitor');
  })
})

function generate_chart() {
  const data = Object.values(traces)
  Plotly.newPlot(chart.value, data, {
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
  });
}
</script>

<template lang="pug">
Navbar
button(type="button" class="position-absolute start-50 top-50 translate-middle btn btn-primary" @click="generate_chart" v-if="show_logs") click here to generate chart
h3(v-else class="position-absolute start-50 top-50 translate-middle") cannot show any chart, please add more logs!
div(ref='chart')
</template>