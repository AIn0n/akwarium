<script setup>
import { useRouter } from 'vue-router';

const props = defineProps(['fish_list']);
const router = useRouter();

function pickFish()
{

}
</script>

<template>
<div class="list-group list-group-flush col-3">
  <a href="#" class="list-group-item list-group-item-action" v-for="fish in props.fish_list">
    {{fish.name}}
      <span v-if="fish.issues.length > 0" class="position-absolute top-50 start-100 translate-middle badge rounded-pill bg-danger">
      {{fish.issues.length}}
      <span class="visually-hidden">problems</span>
    </span>
  </a>
</div>
</template>