<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function gotoMenu(event) {
  router.push("/Aquariums")
}

</script>

<template>
  <div class="container text-center">
    <h3 class="display-4 my-3">Create new aquarium</h3>
    <div class="form-floating w-50 mx-auto my-3">
      <input type="email" class="form-control" placeholder="name@example.com">
      <label for="floatingInput">Aquarium Name</label>
    </div>
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
    <div class="form-floating col mb-3 w-25 mx-auto">
      <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
      <label for="floatingSelect">pump</label>
    </div>
    <div class="dropdown my-3">
    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      Dropdown button
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
    </ul>
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