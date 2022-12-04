<script setup>
import { ref } from 'vue';
import instance from '../configs/axios_instance';

const username = ref('');
const password = ref('');
const rep_password = ref('');
const email = ref('');
const error_message = ref('');
const show_error = ref(false);

function register(event) {
    let result = instance.post("/register", {
        name: username.value,
        password: password.value,
        email: email.value
    }).then( res => { console.log(res)}).catch(e => { 
        //TODO: make this error handling message better
        error_message.value = '' + e;
        show_error.value = true;
    });
}

</script>

<template>
    <h6>
        Don't have account? Register today for free and join the biggest
        base of fish lovers!
    </h6>
    <div class="form-floating mb-1">
        <input v-model="username" type="text" class="form-control" id="floatingInput" placeholder="">
        <label for="floatingInput">Username</label>
    </div>
    <div class="form-floating mb-1">
        <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="">
        <label for="floatingPassword">Password</label>
    </div>
    <div class="form-floating is-invalid mb-1">
        <input v-model="rep_password" type="password" :class="{'form-control':true, 'is-invalid':password !== rep_password}" id="floatingInputGroup2" placeholder="Repeat password" required>
        <label for="floatingInputGroup2">Repeat password</label>
    </div>
    <div class="invalid-feedback" v-show="password !== rep_password">
        passwords must be the same!
    </div>
    <div class="form-floating mb-1">
        <input v-model="email" type="email" class="form-control" id="floatingInput" placeholder="">
        <label for="floatingInput">Email address</label>
    </div>
    <div class="alert alert-danger" role="alert" v-if="show_error">
        {{error_message}}
    </div>
    <div class="btn-group">
        <button type="button" @click="register" class="btn btn-outline-primary">Create account</button>
    </div>
</template>