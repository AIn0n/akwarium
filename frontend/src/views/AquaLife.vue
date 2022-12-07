<script setup>
import { onBeforeMount, ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import instance from '../configs/axios_instance';
import { useAlertsStore } from '../stores/alerts';
import { useRouter } from 'vue-router';

const router = useRouter();
const alertsStore = useAlertsStore();
const species = ref({});

onBeforeMount(()=>{
  const result = instance.get('/species-names')
    .then((res)=>{ species.value = res.data; }).catch((res)=>{
      alertsStore.set_danger("cannot connect to species database, try again later :(")
      router.push("/Aquariums");
    })
});

const specie = ref("");

function pickSpecie(new_specie)
{
  specie.value = new_specie;
  console.log(specie.value);
}

const name = ref("");
const age = ref(0);

function add_fish()
{
}

</script>

<template>
  <Navbar />
  <div class="row">    
    <div class="list-group list-group-flush col-3">
      <a href="#" class="list-group-item list-group-item-action"
      v-for="s in species"
      @click="pickSpecie(s)">
        {{s}}
      </a>
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
      <div class="container text-center row my-3">
        <input type="number" class="form-control col mx-3" placeholder="Age" v-model="age">
        <input type="text" class="form-control col mx-3" placeholder="Name" v-model="name">
        <button type="button" class="btn btn-outline-dark col mx-3" @click="add_fish">
          Add!
        </button>
      </div>
    </div>
  </div>
</template>