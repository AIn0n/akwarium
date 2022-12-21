<script setup>
import Navbar from '../components/Navbar.vue';
import FishList from '../components/FishList.vue';
import { useAquariumStore } from '../stores/aquarium';

const aquariumStore = useAquariumStore();
</script>

<template lang="pug">
Navbar
div(class='row')
  FishList(:fish_list='aquariumStore.aquarium_object.fish')
</template>