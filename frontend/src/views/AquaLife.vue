<script setup>
import Navbar from '../components/Navbar.vue';
</script>

<template>
  <Navbar />
  <div class="row">    
    <div class="list-group list-group-flush col-3">
      <a href="#" class="list-group-item list-group-item-action">fish1</a>
      <a href="#" class="list-group-item list-group-item-action">fish2</a>
      <a href="#" class="list-group-item list-group-item-action">fish3</a>
      <a class="list-group-item list-group-item-action disabled">fish4</a>
    </div>
    <div class="col container text-center  mx-3">
      <h3 class="display-6 my-3">hello again!</h3>
      <div class="row">
        <img src="https://cdn.britannica.com/29/121829-050-911F77EC/freshwater-aquarium.jpg" class="col-5 rounded mx-auto" alt="...">
        <table class="col table table-bordered table-striped table-hover mx-auto">
          <thead class="table-dark">
            <tr>
              <th scope="col">name</th>
              <th scope="col">current</th>
              <th scope="col">minimum</th>
              <th scope="col">maximum</th>
            </tr>
        </thead>
        <tbody>
          <tr>
            <td>NO2</td>
            <td>12</td>
            <td>5</td>
            <td>15</td>
          </tr>
          <tr>
            <td>NO3</td>
            <td>13</td>
            <td>6</td>
            <td>20</td>
          </tr>
        </tbody>
        </table>
      </div>
      <div class="alert alert-warning my-3" role="alert">
        A simple info alert—check it out!
      </div>
      <div class="alert alert-danger my-3" role="alert">
        A simple info alert—check it out!
      </div>
      <div class="container text-center row">
        <button type="button" class="btn btn-outline-dark col mx-3">
          Save logs
        </button>
        <button type="button" class="btn btn-outline-dark col mx-3">
          Back to menu
        </button>
      </div>
    </div>
  </div>
</template>