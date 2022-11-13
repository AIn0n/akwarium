<script setup>
import { ref } from 'vue';
import axios from 'axios';

const username = ref('');
const password = ref('');
const error_message = ref('');
const show_error = ref(false);

function login(event) {
    let config={
        headers: {'Content-Type':'application/x-www-form-urlencoded'}
    }
    let result = axios.post("http://localhost:5000/login", {
        name: username.value,
        password: password.value
    },config).then( res => { console.log(res)}).catch(e => { 
        //TODO: make this error handling message better
        error_message.value = '' + e;
        show_error.value = true;
    });
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
    <div class="alert alert-danger" role="alert" v-if="show_error">
        {{error_message}}
    </div>
    <div class="btn-group">
        <button type="button" @click="login" class="btn btn-outline-primary">login</button>
        <button type="button" class="btn btn-outline-secondary">przypomnij haslo</button>
    </div>
</template>

<style>
</style>