<script setup>
import { ref } from 'vue';
import axios from 'axios';

const username = ref('');
const password = ref('');

function login(event) {
    let result = axios.post("http://localhost:5000/login", {
        name: username.value,
        password: username.value
    }).then( res => {console.log(res.data)});
}
</script>

<template>
    <h1>Login</h1>
    <div class="input-group input-group mb-3">
        <input type="text" v-model="username" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" placeholder="Login">
    </div>
    <div class="input-group input-group mb-3">
        <input type="text" v-model="password" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" placeholder="password">
    </div>
    <div class="btn-group">
        <button type="button" @click="login" class="btn btn-outline-primary">login</button>
        <button type="button" class="btn btn-outline-secondary">przypomnij haslo</button>
    </div>
</template>

<style>
</style>