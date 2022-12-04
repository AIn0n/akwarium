<script setup>
import { useRouter } from "vue-router";
import { ref, onBeforeMount } from 'vue';
import instance from "../configs/axios_instance";

const router = useRouter();

const devices = ref();
const selected = ref({});
const error = ref("");
const aquarium_name = ref("");
const width = ref(0);
const height = ref(0);
const depth = ref(0);

function gotoMenu(event) {
  router.push("/Aquariums")
}

onBeforeMount(()=>{
  let result = instance.get('/devices')
    .then(res => { devices.value = res.data })
    .then((res)=>{
      for (const device in devices.value) {
        selected[device] = null;
      }
    })});

function createAquarium(event)
{
    // TODO: wait for refactor and add all
  let result = instance.post('/add_aquarium', {
    name: aquarium_name,
    height: height,
    width: width,
    length: depth,
    heated_id: selected['heater'],
    lamp_id: selected['lamp'],
    pump_id: selected['pump'],
    filter_id: selected['filter'],

  }).then((res)=>{
    console.log(res);
  }).catch((res)=>{
    error.value = "cannot connect to the server, please try later";
  });
}
</script>

<template>
  <div class="container text-center">
    <h3 class="display-4 my-3">Create new aquarium</h3>
    <div class="form-floating w-50 mx-auto my-3">
      <input type="email" class="form-control" placeholder="name" v-model="aquarium_name">
      <label for="floatingInput">Aquarium Name</label>
    </div>
    <div class="row my-3">
      <div class="input-group mb-3 col">
        <span class="input-group-text">Height</span>
        <input type="number" class="form-control" v-model="height">
      </div>
      <div class="input-group mb-3 col">
        <span class="input-group-text">Width</span>
        <input type="number" class="form-control" v-model="width">
      </div>
      <div class="input-group mb-3 col">
        <span class="input-group-text">Depth</span>
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