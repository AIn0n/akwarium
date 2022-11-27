<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function gotoMenu(event) {
  router.push("/Aquariums")
}

</script>

<template>
  <div class="container text-center">
    <h3 class="display-4">Create new aquarium</h3>
    <div class="row mt-3">
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