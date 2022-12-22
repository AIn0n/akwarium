<script setup>
import { useRouter, useRoute } from 'vue-router';

import { usePickedFishStore } from '../stores/pickedFish.js';

const pickedFishStore = usePickedFishStore();
const props = defineProps(['fish_list']);
const router = useRouter();
const route = useRoute();

function pickFish(fish_name)
{
  pickedFishStore.name = fish_name;
  if (route.path != '/fishPreview')
    router.push('/fishPreview')
}
</script>

<template>
<div class="list-group list-group-flush col-3">
  <a href="#" class="list-group-item list-group-item-action" v-for="fish in props.fish_list" @click="pickFish(fish.name)">
    {{fish.name}}
      <span v-if="fish.issues.length > 0" class="position-absolute top-50 start-100 translate-middle badge rounded-pill bg-danger">
      {{fish.issues.length}}
      <span class="visually-hidden">problems</span>
    </span>
  </a>
</div>
</template>