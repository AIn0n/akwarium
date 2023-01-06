<script setup>
  import Login from '../components/Login.vue'
  import Register from '../components/Register.vue'
</script>

<template>
  <div class="container my-3 w-75">
    <div class="row text-center">
      <div class="col align-self-center">
        <Login/>
      </div>
      <div class="col">
        <Register/>
      </div>
    </div>
  </div>
</template>