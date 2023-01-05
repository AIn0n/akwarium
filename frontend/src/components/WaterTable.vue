<script setup>
const props = defineProps(['water', 'water_min', 'water_max'])

function check_water_row(key)
{
  let curr = props.water[key];
  let min = props.water_min[key];
  let max = props.water_max[key];
  const not_defined = (min === "" && max === "") || (min === undefined && max === undefined);
  if (typeof curr === 'string') { curr = parseFloat(curr); }
  if (typeof min === 'string') { min = parseFloat(min); }
  if (typeof max === 'string') { max = parseFloat(max); }
  return {
    'table-danger': (min > curr || curr > max) && !not_defined,
    'table-warning': (curr == min || curr == max) && !not_defined,
    'table-info': not_defined
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
    <td>{{ props.water_min[key]}}</td>
    <td>{{ val }}</td>
    <td>{{ props.water_max[key]}}</td>
  </tr>
</tbody>
</template>