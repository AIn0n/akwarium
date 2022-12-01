<script setup>
import { useRouter } from "vue-router";
import { ref, onBeforeMount } from 'vue';
import instance from "../configs/axios_instance";

const router = useRouter();

const devices = ref();

function gotoMenu(event) {
  router.push("/Aquariums")
}

onBeforeMount(()=>{
  // TODO: not properly made yet
  let result = instance.get('/devices')
    .then(res => { devices.value = res.data });
});
</script>

<template>
  <div class="container text-center">
    <h3 class="display-4 my-3">Create new aquarium</h3>
    <div class="form-floating w-50 mx-auto my-3">
      <input type="email" class="form-control" placeholder="name@example.com">
      <label for="floatingInput">Aquarium Name</label>
    </div>
    <div class="row my-3">
      <div class="input-group mb-3 col">
        <span class="input-group-text">Height</span>
        <input type="number" class="form-control">
      </div>
      <div class="input-group mb-3 col">
        <span class="input-group-text">Width</span>
        <input type="number" class="form-control">
      </div>
      <div class="input-group mb-3 col">
        <span class="input-group-text">Depth</span>
        <input type="number" class="form-control">
      </div>
    </div>
    <div class="row my-3">
      <div class="form-floating col mx-auto">
        <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
          <option value="1">One</option>
        </select>
        <label for="floatingSelect">pump</label>
      </div>
      <div class="form-floating col mx-auto">
        <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
          <option value="1">One</option>
        </select>
        <label for="floatingSelect">pump</label>
      </div>
      <div class="form-floating col mx-auto">
        <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
          <option value="1">One</option>
        </select>
        <label for="floatingSelect">pump</label>
      </div>
      <div class="form-floating col mx-auto">
        <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
          <option value="1">One</option>
        </select>
        <label for="floatingSelect">pump</label>
      </div>
    </div>
  </div>
  <div class="container text-center w-75">
    <div class="row">
      <button type="button" class="btn btn-primary col mx-3">
        Create!
      </button>
      <button type="button" class="btn btn-secondary col mx-3" @click="gotoMenu">
        Back to menu
      </button>
    </div>
  </div>
</template>