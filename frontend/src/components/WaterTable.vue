<script setup>
const props = defineProps(['water', 'requirements'])

function check_water_row(key)
{
  const curr = props.water[key];
  const min = props.requirements.water_min[key];
  const max = props.requirements.water_max[key];
  console.log(curr, min, max);
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
    <th scope="col">minimum</th>
    <th scope="col">current</th>
    <th scope="col">maximum</th>
  </tr>
</thead>
<tbody>
  <tr v-for="(val, key) in props.water" :class="check_water_row(key)">
    <td>{{ key }}</td>
    <td>{{ props.requirements.water_min[key]}}</td>
    <td>{{ val }}</td>
    <td>{{ props.requirements.water_max[key]}}</td>
  </tr>
</tbody>
</template>