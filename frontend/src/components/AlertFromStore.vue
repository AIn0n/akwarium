<script setup>
import { useAlertsStore } from '../stores/alerts';
const alertStore = useAlertsStore();
</script>

<template>
<div v-if="alertStore.picker_show" :class="alertStore.style" role="alert">
  {{ alertStore.picker_alert }}
  <button type="button" class="btn-close" aria-label="Close" @click="alertStore.reset()"></button>
</div>
</template>