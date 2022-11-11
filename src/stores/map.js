import { ref, computed } from "vue";
import { defineStore } from "pinia";
import polys from "../assets/t2.json";

export const useMapStore = defineStore("map", () => {
  const latLng = ref(undefined);
  const searchResults = ref(undefined);

  const getLatLng = computed(() => {
    return latLng;
  });
  const isSearchActive = computed(() => {
    return latLng !== undefined;
  });
  const getSearchResults = computed(() => {
    return searchResults;
  });

  function search() {
    searchResults.value = polys;
    console.log("in store", searchResults);
  }

  return { latLng, searchResults, isSearchActive, search };
});
