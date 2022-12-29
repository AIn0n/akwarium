<script setup>
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import { useAlertsStore } from '../stores/alerts';

const router = useRouter();
const species = ref({});
const alertsStore = useAlertsStore();

const water_requirements = ref({
  kh: {min: 0, max: 0},
  gh: {min: 0, max: 0},
  no3: {min: 0, max: 0},
  no2: {min: 0, max: 0},
  ph: {min: 0, max: 0}
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
  const result = instance.delete('/delete-species',{'name': specie})
    .then((res)=>{ alertsStore.set_success("sucessfully removed specie: " + specie); })
    .catch((e)=>{ alertsStore.set_danger("cannot remove specie"); });
}

function is_param_invalid(key, water_requirements)
{
  return water_requirements[key].min > water_requirements[key].max ||
          water_requirements[key].min < 0 || water_requirements[key].max < 0;
}

</script>

<template lang="pug">
div(class="container row")
  div(class="col-3 list-group")
    div(class="list-group-item" v-for="specie in species")
      a {{ specie }}
      button(type="button" class="btn-close position-absolute start-100" aria-label="Close")
  div(class="col container text-center")
    h3(class="display-6 mt-3") Admin panel
    div(class="row mx-3")
      div(class="col")
        div(class="input-group my-3")
          span(class="input-group-text") specie name 
          input(type="text" class="form-control")
        div(class="input-group my-3")
          span(class="input-group-text") required velocity
          input(type="number" class="form-control")
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

</template>