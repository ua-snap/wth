<script setup>
import { watch, computed } from "vue";
import { storeToRefs } from "pinia";
import { useMapStore } from "@/stores/map";

// This is how you get the store!  Nice enough.
const mapStore = useMapStore();

// This is what pulls in reactive values from the store.
// It's gotta match the store exports (destructured assignment),
// This seems clunky?  How to watch a single value?
const { searchResults } = storeToRefs(mapStore);

function formatLatLng(latLng) {
  return latLng[0] + ", " + latLng[1];
}
// ?? watch(searchResults, async () => {});
</script>

<template>
  <div class="mx-4">
    <h3 class="title is-3">Search results</h3>
    <h4 class="subtitle is-4" v-if="mapStore.latLng">at {{ formatLatLng(mapStore.latLng) }}</h4>
    <h4 class="title is-5" v-if="searchResults">{{ searchResults[0].features.length }} results</h4>
    <ul v-if="searchResults">
      <li class="mb-2" v-for="feature in searchResults[0].features">
        <span
          class="has-text-weight-bold mr-1 name"
          v-if="
            feature.properties.name &&
            feature.properties.name != feature.properties.hucid
          "
          >{{ feature.properties.name }}</span
        >
        <span class="mr-1 hucId">{{ feature.properties.hucid }}</span>
        <span class="has-text-weight-light hucLevel"
          >HUC{{ feature.properties.huclevel }}</span
        >
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
