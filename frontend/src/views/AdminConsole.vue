<script setup>
import instance from '../configs/axios_instance';
import { useRouter } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import { useAlertsStore } from '../stores/alerts';

const router = useRouter();
const species = ref({});
const alertsStore = useAlertsStore();

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

</script>

<template lang="pug">
div(class="container row")
  div(class="col-3 list-group")
    div(class="list-group-item" v-for="specie in species")
      a {{ specie }}
      button(type="button" class="btn-close position-absolute start-100" aria-label="Close")
  div(class="col container text-center")
    h3(class="display-6 mt-3") Admin panel
    div(class="row")
      div(class="col mx-3")
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
            tr
              th KH
              th
                input(type="number" class="form-control form-control-sm")
              th
                input(type="number" class="form-control form-control-sm")
            tr
              th GH 
              th
                input(type="number" class="form-control form-control-sm")
              th
                input(type="number" class="form-control form-control-sm")
            tr
              th NO3
              th
                input(type="number" class="form-control form-control-sm")
              th
                input(type="number" class="form-control form-control-sm")
            tr
              th NO2
              th
                input(type="number" class="form-control form-control-sm")
              th
                input(type="number" class="form-control form-control-sm")
            tr
              th pH
              th
                input(type="number" class="form-control form-control-sm")
              th
                input(type="number" class="form-control form-control-sm")


</template>