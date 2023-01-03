<script setup>
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import { useAlertsStore } from '../stores/alerts';
import AlertFromStore from '../components/AlertFromStore.vue';

const router = useRouter();
const alertsStore = useAlertsStore();

const species = ref({});
const specie_name = ref("");
const link = ref("");
const velocity = ref(0);
const incompatibles = ref([]);

const water_requirements = ref({
  KH: {min: 0, max: 0},
  GH: {min: 0, max: 0},
  NO3: {min: 0, max: 0},
  NO2: {min: 0, max: 0},
  pH: {min: 0, max: 0}
});

onBeforeMount(()=>{
  const result = instance.get('/species-names')
    .then((res)=>{
      species.value = res.data;
    }).catch((e)=>{
      alertsStore.set_danger("cannot get list of species from server, try later");
      router.push('/Aquariums');
    });
})

function remove_specie(specie)
{
  const result = instance.delete('/delete-species',{data: {name: specie}})
    .then((res)=>{ alertsStore.set_success("sucessfully removed specie: " + specie); })
    .catch((e)=>{ alertsStore.set_danger("cannot remove specie"); });
}

function is_param_invalid(key, water_requirements)
{
  return water_requirements[key].min > water_requirements[key].max ||
          water_requirements[key].min < 0 || water_requirements[key].max < 0;
}

function add_new_specie(name, vel, water_requirements, inc_list, img_link)
{
  const new_specie = {name: name, required_size: vel, image_URL: img_link};
  for (const [key, value] of Object.entries(water_requirements)) {
    new_specie["min_" + key] = value.min;
    new_specie["max_" + key] = value.max;
  }
  const r1 = instance.post('/add-species', new_specie)
    .then((res)=>{ alertsStore.set_success("succesfully added new specie!")})
    .catch((e)=>{ alertsStore.set_danger("cannot add new specie")});

  inc_list.forEach((elem) => {
    instance.post('/add-incompatibilities',{
      subject_name: name,
      aggressor_name: elem
    }).then((res)=> {}).catch((e)=>{
      alertsStore.set_danger("cannot add incompatibility between " + name + " and " + elem);
    })
  });
  console.log(new_specie);
}

</script>

<template lang="pug">
div(class="row container")
  div(class="col-3")
    p(class="text-center fs-4 mt-3") remove species
    div(class="ms-1 list-group container")
      div(class="list-group-item" v-for="specie in species")
        a {{ specie }}
        button(type="button" class="btn-close position-absolute start-100" aria-label="Close" @click="remove_specie(specie)")
  div(class="col container text-center")
    h3(class="display-6 mt-3") Admin panel
    div(class="row mx-3")
      div(class="col")
        div(class="input-group my-3")
          span(class="input-group-text") specie name 
          input(type="text" class="form-control" v-model="specie_name")
        div(class="input-group my-3")
          span(class="input-group-text") link to image
          input(type="text" class="form-control" v-model="link")
        div(class="input-group my-3")
          span(class="input-group-text") required velocity
          input(type="number" class="form-control" v-model="velocity")
        h3(class="display-7") define water requirements
        table(class="table table-dark table-striped")
          thead
            tr
              th parameter 
              th minimum 
              th maximum
          tbody
            tr(v-for="(val, key) in water_requirements" :class="{'table-danger': is_param_invalid(key, water_requirements)}")
              th {{ key }}
              th
                input(type="number" class="form-control form-control-sm" v-model="val.min")
              th
                input(type="number" class="form-control form-control-sm" v-model="val.max")
        div(class="container row align-center my-3")
          button(type="button" class="btn btn-danger col mx-3" @click="add_new_specie(specie_name, velocity, water_requirements, incompatibles, link)") click me
          button(type="button" class="btn btn-danger col mx-3" @click="router.push('/Settings')") back to settings
        AlertFromStore
      div(class="col-3")
        p(class="text-center") Select incompatibles
        select(class="form-select" v-model="incompatibles" multiple)
          option(v-for="specie in species") {{ specie }}

</template>