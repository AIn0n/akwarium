<script setup>
  const props = defineProps(['water', 'requirements'])
  const water = props.water;
  const water_requirements = props.requirements;
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
  <tr v-for="(val, key) in water">
    <td>{{ key }}</td>
    <td>{{ val }}</td>
    <td>{{ water_requirements.water_min[key]}}</td>
    <td>{{ water_requirements.water_max[key]}}</td>
  </tr>
</tbody>
</template>