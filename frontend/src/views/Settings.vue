<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from '../components/Navbar.vue';
import instance from '../configs/axios_instance';
import { useAlertsStore } from '../stores/alerts';

const new_password = ref("");
const new_mail = ref("");
const new_username = ref("");
const alertsStore = useAlertsStore();
const router = useRouter();
const is_admin = ref(false);


instance.get('/if-admin').then((res)=> {
  is_admin.value = res.data.message;
}).catch((res)=>{ is_admin.value = false; })


function change_password()
{
  instance.post('/change-password',{ new_password: new_password.value })
  .then((res) => { alertsStore.set_success("password changed properly :D"); })
  .catch((e)=>{ alertsStore.set_danger("cannot change password"); });
  router.push("/Aquariums");
}

function change_mail() {
  instance.post('/change-email',{new_email: new_mail.value}).then((res)=>{
    alertsStore.set_success("mail changed properly");
  }).catch((res)=>{ alertsStore.set_danger("cannot change mail"); })
  router.push('/Aquariums');
}

function change_username() {
  instance.post('/change-username',{new_email: new_username.value}).then((res)=>{
    alertsStore.set_success("username changed properly");
  }).catch((res)=>{
    alertsStore.set_danger("cannot change username");
  })
  router.push('/Aquariums');
}

</script>

<template>
  <Navbar />
  <div class="d-grip container w-75">
    <button class="container mt-3 btn btn-danger" v-if="is_admin" @click="router.push('/AdminConsole')">go to admin panel</button>
    <div class="card mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change e-mail adress</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New e-mail adress</label>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Input new e-mail adress" aria-label="User's e-mail" aria-describedby="button-addon2" v-model="new_mail">
            <button class="btn btn-success" type="button" id="button-addon2" @click="change_mail">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
    <div class="card mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change password</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New Password</label>
          <div class="input-group mb-3">
            <input v-model="new_password" type="password" class="form-control" placeholder="Input new password" aria-label="User's password" aria-describedby="button-addon2">
            <button class="btn btn-success" type="button" id="button-addon2" @click="change_password">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
    <div class="card mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change Username</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New Username</label>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Input new Username" aria-label="User's username" aria-describedby="button-addon2" v-model="new_username">
            <button class="btn btn-success" type="button" id="button-addon2" @click="change_username">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
  </div>
</template>
