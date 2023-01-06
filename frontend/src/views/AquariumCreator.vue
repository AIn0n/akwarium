<script setup>
import { useRouter } from "vue-router";
import { ref, onBeforeMount, watch } from 'vue';
import instance from "../configs/axios_instance";
import { useAlertsStore } from "../stores/alerts";

const router = useRouter();

const devices = ref();
const selected = ref({});
const error = ref("");
const aquarium_name = ref("");
const width = ref(0);
const height = ref(0);
const depth = ref(0);
const alertsStore = useAlertsStore();
const velocity = ref(0);
const img_link = ref("");


function gotoMenu(event) {
  router.push("/Aquariums")
}

watch([height, width, depth], ([new_height, new_width, new_depth])=>{
  velocity.value = new_height * new_width * new_depth * 0.001;
});

onBeforeMount(()=>{
  let result = instance.get('/devices')
    .then(res => { devices.value = res.data })
    .then((res)=>{
      for (const device in devices.value) {
        selected[device] = null;
      }
    }
)});

function createAquarium(event)
{
  instance.post('/add-aquarium', {
    name: aquarium_name.value,
    height: height.value,
    width: width.value,
    length: depth.value,
    heater_id: selected.value['heater']._id,
    lamp_id: selected.value['light']._id,
    pump_id: selected.value['pump']._id,
    filter_id: selected.value['filter']._id,
    image: img_link.value

  }).then((res)=>{
    alertsStore.set_success("Successfully created new aquarium <3")
    router.push('/Aquariums');
  }).catch((res)=>{
    console.log(res);
    error.value = "cannot connect to the server, please try later";
  });
}
</script>

<template>
  <div class="container text-center w-75">
    <h3 class="display-4 my-3">Create new aquarium</h3>
    <div class="form-floating mx-auto my-3">
      <input type="email" class="form-control" placeholder="name" v-model="aquarium_name">
      <label for="floatingInput">Aquarium Name</label>
    </div>
    <div class="form-floating mx-auto my-3">
      <input type="text" class="form-control" placeholder="name" v-model="img_link">
      <label for="floatingInput"> link for image</label>
    </div>
    <div class="row my-3">
      <div class="input-group col">
        <span class="input-group-text">Height (cm)</span>
        <input type="number" class="form-control" v-model="height">
      </div>
      <div class="input-group col">
        <span class="input-group-text">Width (cm)</span>
        <input type="number" class="form-control" v-model="width">
      </div>
      <div class="input-group col">
        <span class="input-group-text">Depth (cm)</span>
        <input type="number" class="form-control" v-model="depth">
      </div>
    </div>
    <div class="row my-3">
      <div v-for="(val, key) in devices" class="form-floating col mx-auto">
          <div class="card"> 
            <div class="card-header">{{key}}</div>
            <div class="card-body">
              <select class="form-select mb-3" id="floatingSelect" aria-label="Floating label select example" v-model="selected[key]">
                <option v-for="item in val" :value="item">{{item.name}}</option>
              </select>
              <div v-if="(selected[key] != null)">
                <h5 class="card-title">power: {{selected[key].parameter}}</h5>
                <p class="card-text">{{selected[key].description}}</p>
                <p v-if="selected[key].parameter < velocity" class="card-text text-danger"> please choose more powerful device</p>
              </div>
            </div>
          </div>
      </div>
    </div>
    <div class="alert alert-danger" role="alert" v-if="(error.length > 0)">
      {{error}}
    </div>
  </div>
  <div class="container text-center w-75">
    <div class="row">
      <button type="button" class="btn btn-primary col mx-3" @click="createAquarium">
        Create!
      </button>
      <button type="button" class="btn btn-secondary col mx-3" @click="gotoMenu">
        Back to menu
      </button>
    </div>
  </div>
</template>