<script setup>
import { onBeforeMount, ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import instance from '../configs/axios_instance';
import WaterTable from '../components/WaterTable.vue';
import { useAlertsStore } from '../stores/alerts';
import { useAquariumStore } from '../stores/aquarium';
import { useRouter } from 'vue-router';

const router = useRouter();
const alertsStore = useAlertsStore();
const aquariumStore = useAquariumStore();
const species = ref({});
const specie = ref();
const name = ref("");
const age = ref(0);

onBeforeMount(()=>{
  const result = instance.get('/species')
    .then((res)=>{
      species.value = res.data;
    }).catch((res)=>{
      alertsStore.set_danger("cannot connect to species database, try again later :(")
      router.push('/aquaMonitor');
    })
});

function pickSpecie(new_specie) { 
  specie.value = new_specie;
}

function add_fish()
{
  const result = instance.post('/add-fish', {
    name: name.value,
    week_age: age.value,
    species: specie.value.name,
    aquarium_name: aquariumStore.aquarium_name
  }).then((e) => { alertsStore.set_success("successfully added new fish");})
    .catch((e) => {
      alertsStore.set_danger("cannot connect to the server, try again later");
  }).then((res)=>{ router.push('/aquaMonitor'); });
}
</script>

<template>
  <Navbar />
  <div class="row container">
    <!-- here is list column -->    
    <div class="list-group list-group-flush col-3">
      <a href="#" class="list-group-item list-group-item-action"
      v-for="s in species" @click="pickSpecie(s)">{{s['name']}}</a>
    </div>
    <!-- here finish list column -->
    <div v-if="specie !== undefined" class="col container text-center mx-3">
      <h3 class="display-6 my-3">{{specie['name']}}</h3>
      <div class="row">
        <img :src="specie['image_URL']" class="col-5 rounded mx-auto" alt="...">
        <table class="col table table-bordered table-striped table-hover mx-auto">
          <WaterTable :water="aquariumStore.water_object" :water_min="specie.water_requirements.min" :water_max="specie.water_requirements.max" />
        </table>
      </div>
      <div class="container text-center row my-3">
        <p class="mb-3"> incompatible species: {{ specie.incompatibilities.join(', ') }} </p>
        <input type="number" class="form-control col mx-3" placeholder="Age" v-model="age">
        <input type="text" class="form-control col mx-3" placeholder="Name" v-model="name">
        <button type="button" class="btn btn-outline-dark col mx-3" @click="add_fish">
          Add!
        </button>
      </div>
    </div>
    <h3 v-else class="col display-5 my-auto mx-auto text-center">Choose specie</h3>
  </div>
</template>