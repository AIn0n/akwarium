<script setup>
import Navbar from '../components/Navbar.vue';
import { onBeforeMount, ref } from 'vue';
import instance from '../configs/axios_instance';

let aquariums = ref();

onBeforeMount(()=>{
  let result = instance.get('/aquarium')
    .then(res => { aquariums.value = res.data; });
});

</script>

<template>
<Navbar/>
<div class="d-grid gap-5">
  <!-- https://getbootstrap.com/docs/5.2/components/card/#grid-cards -->
  <li v-for="aquarium in aquariums">
    <div class="card text-center w-75 mx-auto">
      <img src="https://cdn.britannica.com/29/121829-050-911F77EC/freshwater-aquarium.jpg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{aquarium.name}}</h5>
        <p class="card-text"></p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </li>
  <div class="card text-center w-75 mx-auto">
      <div class="card-body">
        <h5 class="card-title">Create new aquarium</h5>
        <p class="card-text"></p>
        <a href="#" class="btn btn-primary">+</a>
      </div>
    </div>
</div>
</template>