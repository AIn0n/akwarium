<script setup>
const props = defineProps(['water', 'requirements'])
const water = props.water;
const water_requirements = props.requirements;

function check_water_row(key)
{
  const curr = water[key];
  const min = water_requirements.water_min[key];
  const max = water_requirements.water_max[key];
  return {
    'table-danger': min > curr || curr > max,
    'table-warning': curr == min || curr == max
  };  
}
</script>

<template>
<thead class="table-dark">
  <tr>
    <th scope="col">name</th>
    <th scope="col">current</th>
    <th scope="col">minimum</th>
    <th scope="col">maximum</th>
  </tr>
</thead>
<tbody>
  <tr v-for="(val, key) in water" :class="check_water_row(key)">
    <td>{{ key }}</td>
    <td>{{ val }}</td>
    <td>{{ water_requirements.water_min[key]}}</td>
    <td>{{ water_requirements.water_max[key]}}</td>
  </tr>
</tbody>
</template>