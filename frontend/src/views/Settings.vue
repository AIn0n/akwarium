<script setup>
  import Navbar from '../components/Navbar.vue'
</script>

<template>
  <Navbar />
  <div class="d-grip">
    <div class="card w-75 mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change e-mail adress</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New e-mail adress</label>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Input new e-mail adress" aria-label="User's e-mail" aria-describedby="button-addon2">
            <button class="btn btn-success" type="button" id="button-addon2">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
    <div class="card w-75 mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change password</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New Password</label>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Input new password" aria-label="User's password" aria-describedby="button-addon2">
            <button class="btn btn-success" type="button" id="button-addon2">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
    <div class="card w-75 mx-auto my-3 text-bg-secondary">
      <div class="card-header">Change Username</div>
      <div class="card-body">
        <form class="form-inline">
        <div class="form-group mx-sm-3 mb-1">
          <label for="inputPassword2" class="sr-only">New Username</label>
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="Input new Username" aria-label="User's username" aria-describedby="button-addon2">
            <button class="btn btn-success" type="button" id="button-addon2">Confirm</button>
          </div>
            </div>
        </form>
      </div>
    </div>
  </div>
</template>
