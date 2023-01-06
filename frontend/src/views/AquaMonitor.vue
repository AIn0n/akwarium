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
import { onBeforeMount, ref } from 'vue';
import instance from '../configs/axios_instance';

const aquariumStore = useAquariumStore();
const pickedFishStore = usePickedFishStore();
const alertStore = useAlertsStore();
const router = useRouter();
const downloadLink = ref(null);

const devices = ref({});

async function get_aquarium()
{
  const result = await instance.get("aquarium/" + aquariumStore.aquarium_name)
    .then((res)=>{
      aquariumStore.aquarium_object = res.data;
    }).catch((e)=> {
      alertStore.set_danger("cannot connect to the server " + e);
      router.push('/Aquariums');
    });
}

async function get_devices()
{
  const result = await instance.get('/devices').then((res)=>{
    devices.value['filter'] = res.data['filter'].filter(x => x._id === aquariumStore.aquarium_object.filter_id)[0];
    devices.value['heater'] = res.data['heater'].filter(x => x._id === aquariumStore.aquarium_object.heater_id)[0];
    devices.value['light'] = res.data['light'].filter(x => x._id === aquariumStore.aquarium_object.lamp_id)[0];
    devices.value['pump'] = res.data['pump'].filter(x => x._id === aquariumStore.aquarium_object.pump_id)[0];
  }).catch((e)=>{
    alertStore.set_danger("cannot get devices list");
    router.push('/Aquariums');
  })
}

onBeforeMount(()=>{
  get_aquarium();
  get_devices();
  instance.get('/log-newest/' + aquariumStore.aquarium_name)
    .then((res)=> {
      aquariumStore.water_object = Object.fromEntries(Object.entries(res.data.message).filter(([key]) => key != 'date'));
    }).catch((e)=> {
      alertStore.set_danger("cannot get last log " + e);
    });
  pickedFishStore.name = "";
});

function download() {
  const blob = new Blob([JSON.stringify(aquariumStore.aquarium_object)], {type: 'text/plain'});
  const url = URL.createObjectURL(blob);
  downloadLink.value.href = url;
  URL.revokeObjectURL(url);
}

function import_file(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    instance.post('/import-aquarium', {json_string: e.target.result}).then((res)=>{
      alertStore.set_success("successfully imported aquarium");
    }).catch((e)=>{
      alertStore.set_danger("cannot import aquarium: " + e.response.data);
    });
  }
  reader.readAsText(file)
}
</script>

<template>
  <Navbar />
  <div class="container row text-center">
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
      <table class="table table-sm">
        <thead>
          <th>type</th>
          <th>name</th>
          <th>power</th>
          <th>description</th>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="category in Object.keys(devices)">
            <th>{{ category }}</th>
            <th>{{ devices[category].name }}</th>
            <th>{{ devices[category].parameter }}</th>
            <th>{{ devices[category].description }}</th>
          </tr>
        </tbody>
      </table>
      <div class="text-center row">
        <button type="button" class="btn btn-outline-dark col mx-3">Save logs</button>
        <button type="button" class="btn btn-outline-dark col mx-3" @click="router.push('/WaterParamSetter')">Update Water parameters</button>
        <a ref="downloadLink" class="btn btn-outline-dark col mx-3" download="myfile.txt" @click="download">export to txt file</a>
        <div class="my-3">
          <label for="formFile" class="form-label">import aquarium</label>
          <input type="file" ref="fileInput" class="form-control" id="formFile" @change="import_file"/>
        </div>
      </div>
    </div>
  </div>
</template>