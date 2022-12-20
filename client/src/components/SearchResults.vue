<script setup>
import { watch, computed } from "vue";
import { storeToRefs } from 'pinia'
import { useMapStore } from "@/stores/map";

// This is how you get the store!  Nice enough.
const mapStore = useMapStore();

// This is what pulls in reactive values from the store.
// It's gotta match the store exports (destructured assignment),
// This seems clunky?  How to watch a single value?
const { searchResults } = storeToRefs(mapStore)

</script>

<template>
  <div>
    <h3 class="title is-3">Search results</h3>
    <h4>{{ mapStore.latLng }}</h4>
  </div>
</template>

<style scoped></style>
