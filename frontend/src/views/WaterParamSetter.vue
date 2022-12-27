<script setup>
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';

const router = useRouter();

</script>


<template lang="pug">
h4(class="display-6 text-center my-3") Add water parameters by hand
div(class="row my-3 mx-3")
  div(class="col")
    label(for="khInput" class="form-label") KH 
    input(type="number" class="form-control" id="khInput")
  div(class="col")
    label(for="ghInput" class="form-label") GH
    input(type="number" class="form-control" id="ghInput")
  div(class="col")
    label(for="no3Input" class="form-label") NO3
    input(type="number" class="form-control" id="no3Input")
  div(class="col")
    label(for="no2Input" class="form-label") NO2
    input(type="number" class="form-control" id="no2Input")
  div(class="col")
    label(for="phInput" class="form-label") PH
    input(type="number" class="form-control" id="phInput")
div(class="container my-3 text-center w-75")
  div(class="row")
    button(class="btn btn-primary col mx-3") add new stats
    button(class="btn btn-secondary col mx-3" @click="router.push('/aquaMonitor')") back to aquaMonitor
</template>